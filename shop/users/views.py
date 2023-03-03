from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


from users.forms import UserAuthForm, UserRegistrationForm, UserProfileForm

from django.contrib import auth
from django.shortcuts import render




def auth_user(request):
    if request.method == 'POST':
        form = UserAuthForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

    else:
        form = UserAuthForm()

    context = {'form': form}
    return render(request, 'users/authen.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authen'))
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/registration.html', context)

def profille(request):

    if request.method == 'POST':

        form = UserProfileForm(data=request.Post, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile.html'))
    else:
        form = UserProfileForm()
    context = {'form': form}
    return render(request, 'users/profille.html', context)


def logout(request):
    pass






