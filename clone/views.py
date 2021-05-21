from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Image,Profile,Comment
#from .forms import ProfileForm,CommentForm
from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q


# Create your views here.
def homepage(request):
    current_user=request.user
    image= Image.objects.all()
    comments=Comment.objects.all()
    profiles=Profile.objects.all()


    return render(request,'homepage.html',{"image":image,"comments":comments,"profiles":profiles})
