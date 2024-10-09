from typing import Any, Mapping
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.forms.utils import ErrorList

User = get_user_model()

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
    
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'gender',
            'photo',
            'identity_document_type',
            'identity_document_number',
        ]

class LogInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LogInForm,self).__init__( *args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
    
    class Meta:
        model = User
        fields = "__all__"

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm,self).__init__( *args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
    
    class Meta:
        model = User
        fields = "__all__"

class UpdateProfileForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(UpdateProfileForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
    
    class Meta:
        model = User
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "photo",
            "date_of_birth",
            "identity_document_type",
            "identity_document_number",
        ]