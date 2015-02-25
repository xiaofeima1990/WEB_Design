from django.conf.urls import patterns,url 
from blog import views

urlpatterns = patterns('',
        url(r'^$',views.index, name='index'),
        url(r'^article/(?P<id>\d+)/$',views.content,name='content'),
        url(r'about$',views.about,name='about'),
        url(r'classification$',views.classification,name='classification'),
        url(r'^suggest_article/$', views.suggest_art, name='suggest_art'),
)