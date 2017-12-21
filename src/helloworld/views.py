from django.shortcuts import render
from django.http import HttpResponse
from .models import ShowHelloWorld

def home(request):
	obj = ShowHelloWorld.objects.all()
	html = ''
	for i in obj:
		html+= '<h1>'+i.strn+ '</h1>'
	
	return HttpResponse(html)