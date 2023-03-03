
import django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from users.views import auth_user, register, profille, logout
from django.urls import path

urlpatterns = [
    path('authorization/', auth_user, name='authen'),
    path('registration/', register, name='register'),
    path('profille/', profille, name='profille'),
    path('logout/', logout, name='logout'),
]