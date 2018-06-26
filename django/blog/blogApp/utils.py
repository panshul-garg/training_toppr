from models import Post

import os

from django.contrib.auth.models import User

os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'
user = User.objects.all(pk=1)
for i in range(1,200):
	post=Post(title = 'Some Random Post' , author = user , body = "Lorem ipsum dolor qui officia deserunt mollit anim id est laborum." , status = 'published')
	post.save()
