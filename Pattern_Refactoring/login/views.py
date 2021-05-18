from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.


def loginPage_POST(request):
    if request.user.is_authenticated:
        return redirect('adminpage')
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/adminpage/')
        else:
            return HttpResponseRedirect('/login_before/')
    else:
        messages.error(request, 'Input was invalid!')
        return HttpResponseRedirect('/login_before/')

def loginPage_GET(request):
    if request.user.is_authenticated:
        return redirect('adminpage')
    form = AuthenticationForm()
    if not User.objects.filter(username='testUser').exists():
        User.objects.create_user('testUser', 'test@user.de', 'test')
    return render(request, 'ikindo/login_before.html', {'form': form})

def logoutAction(request):
    logout(request)
    return HttpResponseRedirect('/login_before/')
