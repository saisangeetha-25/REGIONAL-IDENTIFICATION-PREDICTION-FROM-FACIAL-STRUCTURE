"""deepethno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from regional_identification_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('login_action/', views.login_action, name='login_action'),
    path('upload_dataset/', views.upload_dataset, name='upload_dataset'),
    path('upload_action/', views.upload_action, name='upload_action'),
    path('generate_image/', views.generate_image, name='generate_image'),
    path('build_model/', views.build_model, name='build_model'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('registration_action/', views.registration_action, name='registration_action'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_login_action/', views.user_login_action, name='user_login_action'),
    path('user_home/', views.user_home, name='user_home'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('upload_image_action/', views.upload_image_action, name='upload_image_action'),
    path('Recognize/', views.Recognize, name='Recognize'),

]
