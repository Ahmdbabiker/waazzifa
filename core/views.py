from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import *
import datetime
from django.core.mail import send_mail
import requests
from datetime import datetime
from django.utils import timezone
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import FileResponse, Http404
from django.core.paginator import Paginator
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from accounts.models import *
import mimetypes


def homepage(request , tag_id =None):
    
    tags = Category.objects.all()
    job_search = Vacancy.objects.all()
    paginator = Paginator(job_search , 12)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
        

    if request.method == "POST":
        tags = Category.objects.all()
        searched = request.POST.get("job-search")
        side = request.POST.get("side") #gtaa
        jobtype = request.POST.get("jobtype")  #alagd
        location = request.POST.get("location")

        if searched:
            job_search = Vacancy.objects.filter(title__icontains=searched)
            if location:
                job_search = Vacancy.objects.filter(location=location)
            if side:
                job_search = Vacancy.objects.filter(jobtype=side)
            if jobtype:
                job_search = Vacancy.objects.filter(contracttype=jobtype)
        else:
            job_search = Vacancy.objects.none()
       
       

        
        dataa = {"job_search":job_search ,"searched":searched,"dis":searched  , "tags":tags}
        return render (request , 'home.html' , dataa)
    else:
        job_search = Vacancy.objects.all()
        dis = None
        searched = None

    
    if tag_id:
        job_search = Vacancy.objects.filter(tag_id = tag_id)
        paginator = Paginator(job_search , 9)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
    else:
        job_search = Vacancy.objects.all()

  

    data = {'tags':tags , 'job_search':job_search , 'dis':dis ,
    'searched':searched , 'job_search':page_obj, }

    return render(request , 'home.html' , data)

def job_details(request , vacancy_slug):
    user= request.user.id
    if user:
        pro = Profile.objects.get(user__id = user)
    else:
        pass
    vacancy_detail = Vacancy.objects.get(slug = vacancy_slug)
    vacancy_tag = vacancy_detail.tag  # tag of the job
    vacancy_by_tag = Vacancy.objects.filter(tag = vacancy_tag).exclude(slug = vacancy_slug).order_by('?')[:10]

    
    
    count_comments = Comment.objects.filter(vacancy__slug = vacancy_slug)
    commentonjob = Comment.objects.filter(vacancy = vacancy_detail)




    if request.method == 'POST':

        # your existing code here

        # Verify reCAPTCHA response
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': '6LfNpPQpAAAAAOaBqcAwamO_PwqYA_cChLXEz1DQ',
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        response = r.json()
        print(response)
        if response['success']:
            name = request.POST.get("name")
            location = request.POST.get("location")
            date = request.POST.get("date")
            comment = request.POST.get("comment")
            comment_save = Comment.objects.create(name=name, location=location, comment=comment, date=date, vacancy=vacancy_detail)
            messages.success(request, 'تم إضافة التعليق بنجاح!')
        else:
            # reCAPTCHA verification failed, show an error message
            messages.error(request, 'فشل تحقق الCAPTCHA، حاول مرة أخرى.')

    
    data = {"vacancy" : vacancy_detail,
    "pro":pro,
    "vacancy_tag":vacancy_by_tag ,
    "comment_save":commentonjob,
    "count_comments":count_comments}
    return render(request , 'job_details.html' , data)



def companies_emails(request):
    com_emasils = EmailCat.objects.all()
    data = {"com_emails":com_emasils}
    return render(request , 'emails.html', data)



def recaptcha_is_valid(recaptcha_response):
    data = {
        'secret': '6LfNpPQpAAAAAOaBqcAwamO_PwqYA_cChLXEz1DQ',
        'response': recaptcha_response
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    response = r.json()
    return response['success']


def emaildetails(request , category_id):
    emails = EmailCat.objects.get(id= category_id )
    mails = emails.emails_set.all
  
    data = {"emails":mails }
    return render(request , 'email-details.html' , data)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("message")
        send_message = Sendmessage.objects.create(name=name , email=email,
        phone_number = number , message=message)
        messages.success(request, ' شكـرا لك , تم إرسال رسالتك ')


    return render(request , 'contactus.html' ) 


def services(request):
    if request.method == "POST":
        name = request.POST.get("name")
        title= request.POST.get("title")
        phone_no = request.POST.get("phone_no")
        budget = request.POST.get("budget")
        desc = request.POST.get("desc")
        service_create = Service.objects.create(
            name=name , phone_no = phone_no,  title=title,
            budget = budget , desc = desc
        )
        service_create.save()
        messages.success(request, 'تم نشر الخدمـة ')

    
    services = Service.objects.all().order_by('-id')
    paginator = Paginator(services , 8)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)


    
    data = {"services": services , "services":page_obj}
    return render(request , 'services.html' , data)

def service_detail(request , service_id):
    all_service = Service.objects.all().exclude(id = service_id).order_by('?')[:2]
    service_detail = Service.objects.get(id = service_id)
    service_detail.views += 1
    service_detail.save()
    data = {"service_detail":service_detail,
    'all_services':all_service}
    return render(request , 'servicesdetails.html' , data)


def policy(request):
    pass
    return render(request , "policy.html" )


def termspolicy(request):
    pass
    return render(request , "terms-condition.html" )


def createcv(request):
     # your existing code here

    if request.method == "POST":
        # Verify reCAPTCHA response
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': '6LfNpPQpAAAAAOaBqcAwamO_PwqYA_cChLXEz1DQ',
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        response = r.json()
        
        if response['success']:
            fullname = request.POST.get("fullname")
            wazzifa = request.POST.get("wazzifa")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            dob = request.POST.get("dob")
            address = request.POST.get("address")
            linkedurl = request.POST.get("linkedurl")

            languages = request.POST.get("langu")

    # First, save the common fields once in CVorders
            cv_order = CVorders.objects.create(
                fullname=fullname,
                job_title=wazzifa,
                phone=phone,
                email=email,
                dof=dob,
                address=address,
                likndein=linkedurl,
               
                langugaes=languages
            )

            # Education Data
            education_list = request.POST.getlist("education")
            education_names = request.POST.getlist("edname")
            ending_dates = request.POST.getlist("ending_date")

            # Loop through education entries and save them
            for i in range(len(education_list)):
                if education_list[i] and education_names[i] and ending_dates[i]:
                    try:
                        ended_date = datetime.strptime(ending_dates[i], '%Y-%m-%d')
                    except ValueError:
                        ended_date = None  # Handle date parsing error

                    # Save each education entry linked to the CVorders object
                    Education.objects.create(
                        cvorder=cv_order,
                        education=education_list[i],
                        education_name=education_names[i],
                        end_edu_date=ended_date
                    )

    # Work Experience Data
            company_names = request.POST.getlist("company_name")
            positions = request.POST.getlist("position")
            start_dates = request.POST.getlist("start_date")
            end_dates = request.POST.getlist("end_date")
            descriptions = request.POST.getlist("description")

    # Loop through work experience entries and save them
            for i in range(len(company_names)):
                if company_names[i] and positions[i] and start_dates[i] and end_dates[i]:
                    try:
                        start_date = datetime.strptime(start_dates[i], '%Y-%m-%d')
                        end_date = datetime.strptime(end_dates[i], '%Y-%m-%d')
                    except ValueError:
                        start_date, end_date = None, None  # Handle date parsing error

                    # Save each work experience entry linked to the CVorders object
                    WorkExperience.objects.create(
                        cvorder=cv_order,
                        company_name=company_names[i],
                        position=positions[i],
                        start_date=start_date,
                        end_date=end_date,
                        description=descriptions[i] or None
                    )

            # Certificate Data
            certificates = request.POST.getlist("cetianem")

    # Save each certificate entry linked to the CVorders object
            for i in range(len(certificates)):
                if certificates[i]:
                    Certificate.objects.create(
                        cvorder=cv_order,
                        certificate=certificates[i]
                    )

    # Success message
            messages.success(request, 'شكرا لك تم ارسال الطلب')
        else:
    # reCAPTCHA verification failed, show an error message
            messages.error(request, 'فشل تحقق الCAPTCHA، حاول مرة أخرى.')
       
       

    return render(request , 'cvbuilder.html' )



def easy_apply(request, job_id , profile_id):
    if request.method == "POST" and request.user.is_authenticated:
        job = get_object_or_404(Vacancy, id=job_id)
        profile = Profile.objects.get(id=profile_id)
        subject = f"Easy Apply: {job.title}"
        message = f"{request.user.email} is applying for the job: {job.title}\n\nPlease find their CV attached."
        
        # Use your server's email address
        from_email = settings.EMAIL_HOST_USER  # Update with your server email
        recipient_list = [job.applying_email]

        # Create the email
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=recipient_list,
        )
        attachments=[]

        if profile.cv:
            mime_type, _ = mimetypes.guess_type(profile.cv.name)
            attachments.append((profile.cv.name, profile.cv.read(), mime_type or 'application/octet-stream'))
        # Attach Cover Letter
        if profile.cover_letter:
            mime_type, _ = mimetypes.guess_type(profile.cover_letter.name)
            attachments.append((profile.cover_letter.name, profile.cover_letter.read(), mime_type or 'application/octet-stream'))
        # Add attachments to the email
        email.attachments = attachments
            
       
        # Set the Reply-To header
        email.reply_to = [request.user.email]

        try:
            email.send(fail_silently=False)
            return redirect("successsent")
        except Exception as e:
            return HttpResponse(f"حدث خطأ عند إرسال البريد الإلكتروني: {e}")

        
    return HttpResponse("طلب مرفوض")

def emailsent(request):
    subject = f"تم إرسال سيرتك الذاتية"
    message = f"لقد تم بنجاح إرسال سيرتك الذاتية ورسالتك الوظيفية إلى صاحب العمل "
    
    # Use your server's email address
    from_email = settings.EMAIL_HOST_USER  # Update with your server email
    recipient_list = [request.user.email]
    # Create the email
    
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=from_email,
        to=recipient_list,
    )
    email.send()  

    return render(request , "successnt.html")

def view_cv(request ,choise, profile_id):
    profile = Profile.objects.get(id = profile_id)
    if choise == 1:
        if profile:
            try:
                return FileResponse(profile.cv.open('rb'), content_type='application/pdf')
            except FileNotFoundError:
                raise Http404("CV file not found")
        else:
            raise Http404("No CV available")
    elif choise == 2:
        if profile:
            try:
                return FileResponse(profile.cover_letter.open('rb'), content_type='application/pdf')
            except FileNotFoundError:
                raise Http404("CV file not found")
        else:
            raise Http404("No CV available")

def override_cv(request , choises , profile_pk):
    profile = Profile.objects.get(id = profile_pk)
    if profile:
        if choises == 2:
            try:
                pass
            except:
                pass
    else:
        pass

def del_file(request ,profile):
    profile = Profile.objects.get(id = profile)
    if request.method == "POST":
        attr = request.POST.get("cover")
        if attr == '2':
            profile.cover_letter.delete()
            profile.save()
        elif attr == '1':
            profile.cv.delete()
            profile.save()
    return redirect("home")


        

