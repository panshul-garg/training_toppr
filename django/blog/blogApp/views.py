from django.shortcuts import render , get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger


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
	return render( request , 'blogApp/post/detail.html' , { 'post' : post } )