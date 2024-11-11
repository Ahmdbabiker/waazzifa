from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    cv = models.FileField(upload_to="cvs" ,  blank=True, null=True)
    cover_letter = models.FileField(upload_to="coverletters" ,  blank=True, null=True)
    cv_image = models.ImageField(upload_to='cvs', blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save , sender = User)
def createprofile(sender , instance , created , **kwargs):
    if created : 
        Profile(user = instance)