from django.conf.urls import url
from . import views

app_name = 'post'

urlpatterns = [
    url(r'^$', views.get_all_posts, name='get_all_posts'),
    url(r'^post/(?P<id>\d+)$', views.get_post, name='get_post'),
    url(r'^post/create$', views.save_post, name='save_post'),
    url(r'^post/(?P<id>\d+)/edit$', views.edit_post, name='edit_post')
]
