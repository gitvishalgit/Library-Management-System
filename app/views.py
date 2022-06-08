from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm,LoginForm,BookForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import book
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# Create your views here.
def student_view(request):
    bk = book.objects.all()
    return render(request,'students.html',{'books':bk})
# About
# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        bk = book.objects.all()
        return render(request,'dashboard.html',{'books':bk})
    else:
        return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#  User signup Function...
def user_signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations You're register successfully..")
            form.save()
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})

# User Login Function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfull.')
                    return HttpResponseRedirect('/dashboard/')

        else:
            form = LoginForm()
        return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

#Add_Post Function..                     
def add_book(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = BookForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                au=form.cleaned_data['author']
                isb=form.cleaned_data['isbn']
                cat=form.cleaned_data['category']
                bk = book(title=title,author=au,isbn=isb,category=cat)
                bk.save()
                messages.success(request,'Added Successfully..')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = BookForm()
        return render(request,'addbook.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

#Update_Post Function..                     
def update_book(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = book.objects.get(pk=id)
            form = BookForm(request.POST,instance=pi)
            if form.is_valid():
                messages.success(request,'Updated Successfully..')
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = book.objects.get(pk=id)
            form = BookForm(instance=pi)
        return render(request,'updatebook.html',{'form':form})

    else:
        return HttpResponseRedirect('/login/')

#Delete_Post Function..                     
def delete_book(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=book.objects.get(pk=id)
            messages.warning(request,'Deleted')
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


def profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            if request.user.is_superuser == True:
                fm=EditAdminProfileForm(request.POST,instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserProfileForm(request.POST,instance=request.user)
                users=None

            if fm.is_valid():
                messages.success(request,'profile updated!!')
                fm.save()
        else:
            if request.user.is_superuser==True:
                fm=EditAdminProfileForm(instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserProfileForm(instance=request.user)
                users=None
        return render(request,'profile.html',{'name':request.user,'form':fm,'users':users})
    else:
        return HttpResponseRedirect('/login/')

# UserDetail Function
def userdetail(request,id):
    if request.user.is_authenticated:
        pi=User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request,'userdetail.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')