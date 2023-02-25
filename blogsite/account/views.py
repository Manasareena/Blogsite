from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView
from .forms import SignupForm,SignInForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.mail import send_mail


# Create your views here
# class Home(View):
#     def get(self,request):
#         return render(request,"home.html")

# class Signup(View):
#     def get(self,request):
#         form=SignupForm()
#         return render(request,"reg.html",{"form":form})
#     def post(self,request):
#         form_data=SignupForm(request.POST,files=request.FILES)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"Success")
#             return redirect('home')
#         else:
#             messages.error(request,"Failed")
#             return redirect('reg')
# class SignIn(View):
#     def get(self,request):
#         form=SignInForm()
#         return render(request,"login.html",{'form':form})
#     def post(self,request):
#        uname=request.POST.get('username')
#        psw=request.POST.get('password')
#        user=authenticate(request,username=uname,password=psw)
#        if user:
#             login(request,user)
#             return redirect('uhome')
#        else:
#         return redirect("logi")

class SignOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("logi")

class Signup(CreateView):
    model=User
    form_class=SignupForm
    template_name='reg.html'
    success_url=reverse_lazy('home')
    def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
            email_id=form_data.cleaned_data.get('email')
            uname=form_data.cleaned_data.get('username')
            pwd=form_data.cleaned_data.get('password1')
            msg="You are registered in BlogApp.\n Your username"+str(uname)+"\n Password:"+str(pwd)
            form_data.save()
            send_mail(
                'BlogApp Registration',
                msg,
                'manasakuruvattavil@gmail.com',
                [email_id],
                fail_silently=True
                )
            messages.success(request,"Registration Completed")
            return redirect('home')
        else:
            messages.error(request,"Registration failed")
            return render(request,"reg.html",{'form':form_data})

class SignIn(FormView):
    form_class=SignInForm
    template_name='login.html'
    def post(self,request):
       uname=request.POST.get('username')
       psw=request.POST.get('password')
       user=authenticate(request,username=uname,password=psw)
       if user:
            login(request,user)
            return redirect('uhome')
       else:
        return redirect("logi")

class Home(TemplateView):
    template_name="home.html"


        


