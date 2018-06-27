from django.shortcuts import render , get_object_or_404
from .models import Post , Comment
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from .forms import EmailPostForm , CommentForm
from django.core.mail import send_mail


# Create your views here.

def post_list(request):
	posts_list=Post.published.all()
	paginator = Paginator(posts_list , 5)



	print ( "\n\n\n\n" )
	print ( "We have a request" )
	print ( "Scheme  " + str(request.scheme) )
	print ( "Body  " + str( request.body ) )
	print ( "Path " + str( request.path) )
	print ( "Path_Info " + str( request.path_info ))
	print ( "Method " + str  (request.method) )
	print ( "Get" + str (request.GET ) )
	#for post in posts_list:
	#	print (post.get_absolute_url())
	print ( "\n\n\n\n" )

	try:
		page = request.GET['page']
		posts = paginator.page(page)
	except:
		posts=paginator.page(1)

	return render( request , 'blogApp/post/list.html' , { 'posts' : posts } )



def post_detail( request, id ):
	post = get_object_or_404( Post , pk=id )
	comments = post.comments.filter( active = True )
	dummy_variable = "This is the dummy_variable"

	if request.method == 'POST' :
		comment_form = CommentForm( data = request.POST )
		if comment_form.is_valid():
			new_comment = comment_form.save(commit = False)
			new_comment.post = post
			new_comment.save()
	else:
		comment_form = CommentForm()

	return render( request , 'blogApp/post/detail.html' , { 'post' : post , 'comments' : comments , 'comment_form' : comment_form } )


def post_share( request , id ):
	post = get_object_or_404( Post , pk=id )
	sent = False

	if request.method == 'POST' :
		form = EmailPostForm( request.POST )

		if form.is_valid():
			cd = form.cleaned_data
			subject = "{} ({}) recommends you reading '{}' ".format( cd['name'] , cd['email'] , post.title ) 
			message = post.body + '\n' + '{} comment on this '.format( cd['name'] , cd['comments'])
			send_mail( subject , message , 'panshul.garg@toppr.com' , [cd['to']] )
			sent = True

	else:
		form = EmailPostForm()

	return render(request , 'blogApp/post/share.html' , { 'post' : post , 'form' : form , 'sent_mail' : sent})

