from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create', views.create, name='create'),
    url(r'^submit', views.submit, name='submit'),
    url(r'^check', views.check, name='check'),
    url(r'^search', views.search, name='search'),
]