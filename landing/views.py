from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


# Create your views here.

def login_user(request):
    form = UserForm(request.POST)
    user = authenticate(username=request.POST['username'],
                        password=request.POST['password'])
    import pdb; pdb.set_trace()
    if user:
        login(request, user)
        return HttpResponseRedirect(reverse('rq:rq'))
    return render(request, 'landing/landing.html', {'form': form})


def register_user(request):
    form = UserForm(request.POST)
    if not form.is_valid():
        return render(request, 'landing/landing.html', {'form': form})
    User.objects.create_user(username=request.POST['username'],
                             password=request.POST['password'])
    new_user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
    if new_user.is_authenticated():
        login(request, new_user)
        return HttpResponseRedirect(reverse('rq:rq'))
    return render(request, 'landing/landing.html', {'form': form})


def land(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            return login_user(request)
        elif 'register' in request.POST:
            return register_user(request)
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('rq:rq'))
        form = UserForm()
        return render(request, 'landing/landing.html', {'form': form})


def logout_view(request):
    logout(request)
    form = UserForm()
    return render(request, 'landing/landing.html', {'form': form, 'nbar': 'logout'})
