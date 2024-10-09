from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self,email,password,**kwargs):
        if not email:
            raise ValueError("E-mail is required.")
        user = self.model(email=email,**kwargs)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**kwargs):
        kwargs.setdefault("is_staff",True)
        kwargs.setdefault("is_superuser",True)
        
        if kwargs.setdefault("is_superuser") is not True:
            raise ValueError("SuperUser must be True")
        return self._create_user(email,password,**kwargs)


blood_group_choice = [
    ("A+","A Positive (A+)"),
    ("A","A Negative (A-)"),
    ("B+","B Positive (B+)"),
    ("B-","B Negative (B-)"),
    ("O+","O Positive (O+)"),
    ("O-","O Negative (O-)"),
    ("AB+","AB Positive (AB+)"),
    ("AB-","AB Negative (AB-)"),
]
identity_choices = [
    ("nid","National ID"),
    ("passport","Passport"),
    ("birth_certificate","Birth Certificate"),
]

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=250,unique=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    middle_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    date_of_birth = models.DateField(null=True,blank=True,help_text="Enter the Field in this format : Year-Month-Day")
    gender = models.CharField(max_length=2,choices=[("M","Male"),("F","Female"),("O","Other")])
    blood_group = models.CharField(max_length=12,null=True,blank=True,choices=blood_group_choice)
    identity_document_type = models.CharField(max_length=50,choices=identity_choices)
    identity_document_number = models.CharField(max_length=100)
    photo = models.ImageField(null=True,upload_to="profileImage/")
    date_joined = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name"]
    
    def get_full_name(self):
        return str(self.first_name) + " " + str(self.middle_name) + " " + str(self.last_name)
    
    objects = UserManager()
    
    
    