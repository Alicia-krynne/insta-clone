from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
#from django.db.models import Q


Gender=(
    ('Male','Male'),
    ('Female','Female'),
)
# Create your models here.
class Image(models.Model):
    image= models.ImageField(upload_to="media/")
    name=models.CharField(max_length=200)
    caption= models.TextField(max_length=600)
    profile = models.ForeignKey('Profile',models.SET_NULL,null=True)
    likes = likes = models.IntegerField()
    comments=models.TextField(max_length=600)
    
    def __str__(self):
        return self.name
    
    def save_image(self):
          self.save()
        
    def update_caption(self):
        self.save()

    def delete_image(self):
        self.delete()

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profilepics/',null= True)
    bio = HTMLField(blank=True)
    name = models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    phonenumber = models.IntegerField(blank=True)
    gender = models.CharField(max_length=15,choices=Gender,default="Male")

    def __str__(self):
        return self.name
    
    def save_profile(self):
          self.save()
        
    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Comment(models.Model):
    comment = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def save_comment(self):
        self.save()