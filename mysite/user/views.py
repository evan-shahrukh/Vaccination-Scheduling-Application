from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseBadRequest
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login as user_login,logout as user_logout,update_session_auth_hash

from user.forms import SignUpForm,LogInForm,ChangePasswordForm,UpdateProfileForm
from user.email import send_email_verification
from user.utils import EmailVerificationTokenGenerator

from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

User = get_user_model()

# Create your views here.

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created Successfully")
            return HttpResponseRedirect(reverse("index"))
        context = {
            'form' : form
        }
        messages.error(request,"Please enter valid data!")
        return render(request,"./user/signup.html",context)
    context = {
        'form' : form
    }
    return render(request,"./user/signup.html",context)

def login(request):
    form = LogInForm()
    if request.method == "POST":
        form = LogInForm(request,request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email,password=password)
            if user is not None:
                user_login(request,user)
                messages.success(request,"Successfully logged in !!!")
                return HttpResponseRedirect(reverse("index"))
            messages.error(request,"Please enter valid Credential !!!")
            HttpResponseRedirect(reverse("account:login"))
            
        context = {
            "form" : form,
        }    
        messages.error(request,"Please enter valid Credential !!!")
        return HttpResponseRedirect(reverse("account:login"))
        
    context = {
        'form' : form,
    }
    return render(request,"./user/login.html",context)

def logout(request):
    user_logout(request)
    messages.info(request,"Logged out successfully !!!")
    return HttpResponseRedirect(reverse("account:login"))

def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,"Password  have been changed successfully !!!")
            return HttpResponseRedirect(reverse("index"))
        context = {
            'form' : form
        }   
        messages.error(request,"Please enter valid credential !!!")
        render(request,"./user/change-password.html",context)
    context = {
        'form' : ChangePasswordForm(request.user)
    }
    return render(request,"./user/change-password.html",context)

def profile_view(request):
    context = {
        "user" : request.user
    }
    return render(request,"./user/profile-view.html",context)

def update_profile(request):
    if request.method == "POST":
        form = UpdateProfileForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile successfully updated !!!")
            return HttpResponseRedirect(reverse("account:profile-view"))
        
        context = {
            "form" : form
        }
        messages.error(request,"Please enter valid data !!!")
        return render(request,"./user/update-profile.html",context)
    context = {
        'form' : UpdateProfileForm(instance=request.user)
    }
    return render(request,"./user/update-profile.html",context)

def email_verification_request(request):
    if not request.user.is_email_verified:
        send_email_verification(request,request.user.id)
        return HttpResponse("E-mail verification link sent to your address.")
    return HttpResponseForbidden("E-mail already verified.")

def send_email_verify(request,uidb64,token):
    try:
        user_id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=user_id)
    except:
        user = None

    if user == request.user:
        if EmailVerificationTokenGenerator.check_token(user,token):
            user.is_email_verified = True
            user.save()
            messages.success(request,"E-mail has been activated!")
            return HttpResponseRedirect(reverse("account:profile-view"))
        return HttpResponseBadRequest("Invalid request.")
    return HttpResponseForbidden("You don't have permission to use this link.")
    
        
