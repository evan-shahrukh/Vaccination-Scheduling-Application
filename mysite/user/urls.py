from django.urls import path
from user.views import signup,login,logout,change_password,profile_view,update_profile,email_verification_request,send_email_verify

app_name="account"

urlpatterns = [
    path("signup/",signup,name="signup"),
    path("login/",login,name="login"),
    path("logout/",logout,name="logout"),
    path("change_password/",change_password,name="change-password"),
    path("profile_view/",profile_view,name="profile-view"),
    path("update_profile/",update_profile,name="update-profile"),
    path("email_verification/",email_verification_request,name="update-verification"),
    path("email/activate/<uidb64>/<token>/",send_email_verify,name="email-activate"),
]
