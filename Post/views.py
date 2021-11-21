from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm,PostForm
from .models import Post
#message
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    form=PostForm()
    user=request.user
    #print(user)
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=user
            post.save()
            return redirect("home")
            
        else:
            messages.info(request,"Something went wrong")
    post=Post.objects.using("post_db").all()
    context={
        'form':form,
        'post':post
    }
    return render(request,"Post/home.html",context)

def login_view(request):
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(User,username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")
            
        else:
            return redirect("login")
    else:
        context={
            "user":User
        }
        return render(request,"Post/login.html",context)

def register_view(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
        else:
            messages.info(request,"Fill in the details")
            
    else:
        
        form=SignUpForm()
        return render(request,"Post/register.html",{"form":form})
    
def logout_view(request):
    logout(request)
    return redirect('login')
