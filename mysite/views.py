from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect

def login(request):
	c = {}
	# c.update(context(request))
	return render(request, 'polls/login.html',c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username,password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/loggedin')
	else:
		return HttpResponseRedirect('/invalid')


def loggedin(request):
	return render_to_response('polls/loggedin.html',
                             {'full_name':request.user.username})

def invalid_login(request):
	return render_to_response('polls/invalid_login.html') 


def logout(request):
	auth.logout(request)
	return render_to_response('polls/logout.html')

	


