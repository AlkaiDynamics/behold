import openai
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .forms import ImageForm, StyleForm, UserRegistrationForm, UserLoginForm
from .models import Image, Style, GeneratedText
from django.conf import settings
from google.cloud import vision
from google.oauth2 import service_account
from google.api_core.exceptions import GoogleAPIError

# Set up the OpenAI API key from settings
openai.api_key = settings.OPENAI_API_KEY

# Google Cloud Vision API client setup
def get_vision_client():
    credentials = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_CLOUD_VISION_CREDENTIALS_PATH
    )
    return vision.ImageAnnotatorClient(credentials=credentials)

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            messages.success(request, 'Image uploaded successfully.')
            return redirect('style_selection', image_id=image.id)
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

@login_required
def style_selection(request, image_id):
    try:
        image = Image.objects.get(id=image_id, user=request.user)
    except Image.DoesNotExist:
        messages.error(request, 'Image not found.')
        return redirect('upload_image')

    if request.method == 'POST':
        form = StyleForm(request.POST)
        if form.is_valid():
            style = form.save(commit=False)
            style.save()
            return redirect('generate_text', image_id=image_id, style_id=style.id)
    else:
        form = StyleForm()
    return render(request, 'style_selection.html', {'form': form, 'image': image})

@login_required
def generate_text(request, image_id, style_id):
    from . import services

    result, error = services.text_generation_service.generate_text_for_image_style(request.user, image_id, style_id)
    if error:
        messages.error(request, error)
        return redirect('style_selection', image_id=image_id)
    text_instance_id = result.get('text_instance_id')
    messages.success(request, 'Text generated successfully.')
    return redirect('result', text_id=text_instance_id)

@login_required
def result(request, text_id):
    try:
        generated_text = GeneratedText.objects.get(id=text_id, image__user=request.user)
        return render(request, 'result.html', {'generated_text': generated_text.text})
    except GeneratedText.DoesNotExist:
        messages.error(request, 'Generated text not found.')
        return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html', {'form': form})

@login_required
def account(request):
    return render(request, 'account.html')

@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

