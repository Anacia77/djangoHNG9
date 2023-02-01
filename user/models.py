from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models 

class Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=64, null=True)
    profile_pic = models.FileField(default="user2.png", null=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_detail(sender, instance, created, **kwargs):
    if created:
        Detail.objects.create(user=instance)
        print('Profile created')

#post_save.connect(create_detail, sender=User)

def update_detail(sender, instance, created, **kwargs):
    if created == False:
        instance.detail.save()
        print('Profile updated')

#post_save.connect(update_detail, sender=User)


#      <img class="profile_pic" src="{{request.user.detail.profile_pic.url}}" style="width:150px" alt="">