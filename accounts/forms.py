from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import forms
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', )

class ProfileForm(forms.modelForm):
    class Meta:
        model = Profile
        fields = ('image', )