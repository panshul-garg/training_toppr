from django.contrib import admin

from .models import Post , Comment

class PostAdmin( admin.ModelAdmin ):
	list_display = ('title' , 'slug' , 'author' , 'publish' , 'status' )
	prepopulated_fields = { 'slug' : ( 'title', )}

admin.site.register( Post , PostAdmin )

class CommentAdmin( admin.ModelAdmin ):
	list_display = ('name' , 'email' , 'post' , 'created' , 'updated')
	search_fields = ( 'name' , 'email' , 'body' )

admin.site.register( Comment , CommentAdmin )

# Register your models here.
