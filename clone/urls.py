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


    #url(r'^new/location$',views.new_location, name='new-location'),
#     url(r'^profile/',views.profile, name='profile'),
#     url(r'^edit/profile$',views.edit_profile, name='edit-profile'),
#     url(r'^explore/',views.explore, name='explore'),
#     url(r'^like/$', views.like, name='like'),
#     url(r'^search/',views.search_results, name='search_results'),
#     url(r'^user-profile/(\d+)',views.userprofile,name='user-profile'),
#     # url(r'^user-profile/(?P<username>\w{0,50})',views.userprofile,name='user-profile'),
#     
#     url(r'^change_profile/(?P<username>\w{0,50})',views.change_profile,name='change_profile'),
 ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)