from django.contrib import admin
from .models import  Profile,Image,Comment
# Register your models here.


#class ArticleAdmin(admin.ModelAdmin):
    #filter_horizontal =('tags',)


admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)