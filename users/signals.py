from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
#@receiver(post_save,sender=Profile)
def createProfile(sender,instance, created,**kwargs):
    #print('Profile signal triggered')
    #print('Profile Saved ')   #this printing statement appears in the cmd prompt 
    #print('Instance:',instance)
    #print('CREATED: ',created)  #created tells whether the database is created now or earlier by a boolean value
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,

        )
        subject="Welcome to Devsearch"
        message="We are glad you are here!"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    if created==False:
        user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()

def deleteUser(sender,instance,**kwargs):
    user=instance.user
    user.delete()
    

post_save.connect(createProfile, sender=User) #the post_save signal gets connected when the profile model
#send the data and the profile gets updated this signal gets received 
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser,sender=Profile)  

#we can use the decorator instead of the above code
