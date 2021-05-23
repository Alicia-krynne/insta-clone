from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Image,Profile,Comment
from .forms import ProfileForm,CommentForm,ImageForm
from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
#from django.db.models import Q


# Create your views here.
def homepage(request):
    current_user=request.user
    image= Image.objects.all()
    comments=Comment.objects.all()
    profiles=Profile.objects.all()


    return render(request,'homepage.html',{"image":image,"comments":comments,"profiles":profiles})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = Profile.search_profile(search_term)
        message=f"{search_term}"

        return render(request,'search.html',{"message":message,"users":searched_users})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.username = current_user
            image.profile_pic = profile.profile_pic

            image.likes=0

            image.save()

        return redirect('Homepage')

    else:
        form = ImageForm()

    return render(request,'new_image.html',{"form":form})    

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    current_user_id=request.user.id
    form=CommentForm()
    comments=Comment.objects.all()
    comment_number=len(comments)
    print(current_user)
    # print(current_user_id)

    image_id = None
    if request.method == 'GET':
        image_id = request.GET.get('image_id')

    likes = 0
    if image_id:
        image = Image.objects.get(id=int(image_id))
        if  image:
            likes = image.likes + 1
            image.likes =  likes
            image.save()
            print(likes)

        return redirect('profile.html')

    try:
        profile = Profile.objects.get(username=current_user)
        image = Image.objects.filter(name=current_user)
        title = profile.name
        username = profile.username
        image_number= len(image)
        
    except ObjectDoesNotExist:
        return redirect('edit-profile')


    return render(request,"profile.html",{"profile":profile,"image":image,"form":form,"image_number":image_number,"title":title,"username":username,"comments":comments,"comment_number":comment_number})

@login_required(login_url='/accounts/login/')
def like(request):
    image_id = None
    if request.method == 'GET':
        imag_id = request.GET.get('image_id')

    likes = 0
    if image_id:
        image = Image.objects.get(id=int(image_id))
        if image:
            likes = image.likes + 1
            image.likes =  likes
            image.save()
            print(likes)
    return HttpResponse(likes)

def comment(request):
    print("AJAX is working")

    comment = request.GET.get('comment')
    image = request.GET.get('image')
    username = request.user

    comment = Comment(comment=comment,image=image,username=username)
    comment.save()

    recent_comment= f'{Comment.objects.all().last().comment}'
    recent_comment_user = f'{Comment.objects.all().last().username}'
    data= {
        'recent_comment': recent_comment,
        'recent_comment_user':recent_comment_user
    }

    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.username = current_user
            profile.save()

    else:
        form=ProfileForm()

    return render(request,'edit_profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def userprofile(request,profile_id):
    current_user=request.user
    form =CommentForm()
    comments=Comment.objects.all()

    try:
        all_images=Image.objects.all()
        profile = Profile.objects.get(id=profile_id)
        prof_username = profile.username
        image = Image.objects.filter(username=prof_username)
    except:
        raise ObjectDoesNotExist()
    return render(request,"user-profile.html",{"profile":profile,"image":image,"form":form,"comments":comments})


@login_required(login_url='/accounts/login/')
def change_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.username = current_user
            caption.save()
        return redirect('index')
    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'change_profile.html',{"form":form})