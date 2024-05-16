from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image, Style

class ImageForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}),
        help_text='Enter a description for the image.',
        required=False
    )

    class Meta:
        model = Image
        fields = ['description', 'image_file']
        help_texts = {
            'image_file': 'Upload an image file.',
        }
        widgets = {
            'image_file': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class StyleForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = ['type', 'tone', 'voice', 'length']
        help_texts = {
            'type': 'Select the style of writing you prefer.',
            'tone': 'Choose the tone that should be used.',
            'voice': 'Choose a voice for your content.',
            'length': 'Specify the length of the content in words.',
        }
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'tone': forms.Select(attrs={'class': 'form-control'}),
            'voice': forms.Select(attrs={'class': 'form-control'}),
            'length': forms.NumberInput(attrs={'min': 100, 'max': 2000}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='A valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': '150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Add custom validation logic
        if 'example' in username:
            raise forms.ValidationError("Username may not contain 'example'.")
        return username

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, help_text='Enter your username.')
    password = forms.CharField(widget=forms.PasswordInput, help_text='Enter your password.')
