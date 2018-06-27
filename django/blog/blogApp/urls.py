from django.conf.urls import url
from . import views
 

app_name = 'blogApp'
urlpatterns = [
	url( r'^$' , views.post_list , name = 'post_list') ,
	url( r'^(?P<id>[0-9]+)/$' , views.post_detail , name = 'post_detail'),
	url( r'^(?P<id>[0-9]+)/share/$' , views.post_share , name = 'post_share'),

]