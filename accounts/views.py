from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login , logout 
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import authenticate 
from .tokens import account_activation_token
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.encoding import force_str
from core.models import *
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode 
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes 
from django.contrib.sites.shortcuts import get_current_site
from .models import *

from PIL import Image
from django.contrib import messages 



def send_verification_email(user, request):
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    site = get_current_site(request)
    mail_subject = 'Activate your account'
    message = render_to_string('authentication/activation_email.html', {
        'user': user,
        'domain': site.domain,
        'uid': uid,
        'token': token,
    })
    send_mail(mail_subject, message, 'ahmd.django@gmail.com', [user.email])


def activate(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64)) 
        user = User.objects.get(pk=uid) 
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None  
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True  
        user.save()
        login(request, user)
       
        return redirect('addfiles')
    else:
        return HttpResponse('Activation link is invalid!')  



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # Basic validation
        if password1 != password2:
            return render(request, 'authentication/register.html', {'error': 'Passwords do not match'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'authentication/register.html', {'error': 'Username already exists'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'authentication/register.html', {'error': 'Email already in use'})
        
        user = User.objects.create_user(username=username, email=email, password=password1 , is_active = False)

            
        send_verification_email(user, request)
        
      
        return redirect('registration_complete')
    
    return render(request, 'customerRegister.html')


def registration_complete(request):
    pass
    return render(request , "registration_complete.html")



def loggining(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('pass')

        user = authenticate(request , username = name , password = password)
        
        if user is not None :
            login(request , user)
            return redirect('home')
        else:
            return render(request , 'loginnew.html' , {'error':'invalid credentials'})
    else:
        return render(request , 'loginnew.html')


def add_files(request):
    if request.method == "POST":
        name =  request.POST.get("name")
        phoneno = request.POST.get("phoneno")
        cv = request.FILES.get("cv")
        cover_letter = request.FILES.get("coverletter")
        
        save_filese = Profile.objects.create(
        user = request.user , phone_number = phoneno , 
        cv = cv , cover_letter = cover_letter)
        
        return redirect("home")
    return render(request , "addCV.html" )


def profile_data(request , profile_id ):
    try:
        get_profile = Profile.objects.get(user__id = profile_id)
    except:
        messages.error(request , "you dont have profile")
        return redirect("home")
    data = {"profile":get_profile}
    return render(request , "profile.html" , data )



def logginout(request):
    logout(request)
    return redirect('home')


























