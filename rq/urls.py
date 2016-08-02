from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='rq'),
    url(r'^sq/', views.submitq, name='sq'),
    url(r'^aq/', views.asked, name='aq'),
]
