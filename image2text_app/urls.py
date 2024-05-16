from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_image, name='upload_image'),
    path('style/<int:image_id>/', views.style_selection, name='style_selection'),
    path('generate/<int:image_id>/<int:style_id>/', views.generate_text, name='generate_text'),
    path('result/<int:text_id>/', views.result, name='result'),
    path('user/register/', views.register, name='register'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/account/', views.account, name='account'),
    path('accounts/login/', views.login, name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),
]

