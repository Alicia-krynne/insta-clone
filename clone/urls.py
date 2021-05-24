from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.homepage,name='Homepage'),
    path('search/',views.search_results,name='search_results'),
    path('new/image',views.new_image, name='new-image'),
    path ('profile/',views.profile,name='profile'),
    path('comment/',views.comment,name='comment'),
    path('like/', views.like, name='like'),
    path('edit/profile',views.edit_profile, name='edit-profile'),
    path('user-profile/',views.userprofile,name='userprofile'),
    path('change_profile/',views.change_profile,name='change_profile'),



 ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)