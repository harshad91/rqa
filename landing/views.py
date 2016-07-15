from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

# Create your views here.

def land(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		new_user= authenticate(username=request.POST['username'], 
			password=request.POST['password'])
		if not new_user:
			if not form.is_valid():
				return render(request,'landing/landing.html', {'form': form})
			new_user = User.objects.create_user(username=request.POST['username'], 
				password=request.POST['password'])
			new_user = authenticate(username=request.POST['username'], 
				password=request.POST['password'])
			if new_user.is_authenticated():
				login(request, new_user)
				return HttpResponseRedirect(reverse('rq:rq'))

		elif new_user.is_authenticated():
			login(request, new_user)
			return HttpResponseRedirect(reverse('rq:rq'))				
	else:
		if request.user.is_authenticated():
			return HttpResponseRedirect(reverse('rq:rq'))
		form = UserForm()
	return render(request,'landing/landing.html', {'form': form})

def logout_view(request):
	logout(request)
	form = UserForm()
	return render(request,'landing/landing.html', 
					{'form': form, 'nbar': 'logout'})
