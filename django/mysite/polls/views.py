from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
	print ("\n\n\n\n")
	print (request)
	print ("\n\n\n\n")
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	template=loader.get_template("polls/index.html")
	context={
		'latest_question_list':latest_question_list,
	}
	return HttpResponse(template.render(context,request))

def detail(request,question_id):
	print ("\n\n\n\n")
	print (request)
	print (question_id)
	print ("\n\n\n\n") 
	return HttpResponse("You are looking at question %s." %question_id)


def results(request,question_id):
	print ("\n\n\n\n")
	print (request)
	print (question_id)
	print ("\n\n\n\n")
	response= "You are looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request,question_id):
	print ("\n\n\n\n")
	print (request)
	print (question_id)
	print ("\n\n\n\n")
	return HttpResponse("You are voting on question %s" % question_id )