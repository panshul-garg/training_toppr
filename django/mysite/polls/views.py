from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice

# Create your views here.
def index(request):
	print ("\n\n\n\n")
	print (request)
	print ("\n\n\n\n")
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	#template=loader.get_template("polls/index.html")
	context={
		'latest_question_list':latest_question_list,
	}
	print (context)
	#question=get
	#return HttpResponse(template.render(context,request))
	return render(request,'polls/index.html',context)

def detail(request,question_id):
	print ("\n\n\n\n")
	print (request)
	print (question_id)
	print ("\n\n\n\n") 

	question=get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
			'question':question,
			'error_message': "You didn't select a choice"
			})
	else:
		selected_choice.vote+=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))
	return render(request,'polls/detail.html',{'question':question})


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