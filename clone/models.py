from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
#from django.db.models import Q

# Create your models here.
class Image(models.Model):
    image= models.ImageField(upload_to="media/")
    name=models.CharField(max_length=200)
    caption= models.TextField(max_length=600)
    profile = models.ForeignKey('Profile',models.SET_NULL,null=True)
    likes = likes = models.IntegerField()
    comments=models.TextField(max_length=600)
    
    def __str__(self):
        return self.title
    
    def save_image(self):
          self.save()
        
    def update_image(self):
        self.save()

    def delete_image(self):
        self.delete()
        
