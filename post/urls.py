from django.conf.urls import url,include
from . import views

app_name='post'

urlpatterns = [
    url(r'^create/', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
]
