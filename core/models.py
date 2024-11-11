from django.db import models
from django.utils.text import Truncator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    CHOISES = (
        ('abudhabi' , 'أبوظبي'),
        ('dubai' , 'دبي'),
        ('sharjah' , 'الشارقة'),
        ('fujairah' , 'الفحيرة'),
        ('rak' , 'راس الخيمة'),
        ('ajman' , 'عجمان'),
    )

    WORKTYPE = (
        ('full' , 'دوام كامل'),
        ('part' , 'دوام جزئي'),
        ('remot' , 'عمل عن بعد')
    )

    CHOISES2 = (
        ('spec' , 'جهة خاصة'),
        ('gover' , 'جهة حكومية'),
    )

    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length = 20 , null=True)
    tag = models.ForeignKey(Category , on_delete=models.CASCADE)
    contracttype = models.CharField(max_length=10 ,null=True, choices=WORKTYPE)
    jobtype = models.CharField(max_length=10 , choices=CHOISES2)
    location = models.CharField(max_length=10 , choices=CHOISES)
    desc = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    applying = models.CharField(max_length=50 , null=True)
    applying_email = models.CharField(max_length=255,null=True , blank=True)
    
    def count_comments(self):
        return Comment.objects.get(vacancy = self ).count()


    def __str__(self):
        return Truncator (self.title).chars(40)


class Comment(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=15)
    comment  = models.TextField(null=True)
    date = models.DateField(null=True)
    vacancy = models.ForeignKey(Vacancy , on_delete=models.CASCADE , related_name='vacancies')
    date_commented = models.DateTimeField(auto_now_add=True , null=True)

 
    def __str__(self):
        return f"{self.name} commented on {self.vacancy}"


class EmailCat(models.Model):
    name = models.CharField(max_length=40 , null=True)

    def __str__(self):
        return self.name


class Emails(models.Model):
    name = models.CharField(max_length=40 , null= True)
    contact = models.CharField(max_length=30)
    specialist = models.ForeignKey(EmailCat , on_delete=models.CASCADE , null=True)

    def __str__(self):
        return f"{self.name} contact:: {self.contact}"


class Advertisement(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    whatsapp_no = models.IntegerField(null=True)
    def __str__(self):
        return f"{self.name} orderd in {self.date_ordered}"


class Service(models.Model):
    name =  models.CharField(max_length=40)
    phone_no = models.IntegerField()
    title = models.CharField(max_length=30)
    budget = models.IntegerField()
    desc = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} posted a service {self.title}"

class Sendmessage(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.TextField()


    def __str__(self):
        return f"{self.name} sent a Message"








class CVorders(models.Model):
    fullname = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20 ,  null=True)
    email = models.EmailField( null=True)
    dof = models.DateField()
    address = models.TextField( null=True)
    likndein = models.URLField(null=True, blank=True)
    skill = models.CharField(max_length=255 , null=True)
    langugaes = models.CharField(max_length=255 , null=True)

class Education(models.Model):
    CHIOSES = (
        ("A" , "لا يوجد"),
        ("B" , "ثانوي"),
        ("C" , "جامعي"),
    )

    cvorder = models.ForeignKey(CVorders, on_delete=models.CASCADE, related_name='educations')
    education = models.CharField(max_length=255 ,choices=CHIOSES )
    education_name = models.CharField(max_length=255)
    end_edu_date = models.DateField(null=True, blank=True)

class WorkExperience(models.Model):
    cvorder = models.ForeignKey(CVorders, on_delete=models.CASCADE, related_name='work_experiences')
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True, blank=True)

class Certificate(models.Model):
    cvorder = models.ForeignKey(CVorders, on_delete=models.CASCADE, related_name='certificates')
    certificate = models.CharField(max_length=255)
