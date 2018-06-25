from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	print ("\n\n\n\n")
	print (request)
	print ("\n\n\n\n")
	return HttpResponse("Hello World")

