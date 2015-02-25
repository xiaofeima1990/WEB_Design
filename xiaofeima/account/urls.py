from django.conf.urls import patterns, include, url
from django.conf import settings
from account import views



urlpatterns = patterns('',
     url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
     url(r'^login/$', views.user_login, name='login'), 
     url(r'^profile/$', views.profile, name='profile'),
     
     url(r'^$', views.index, name='index'),
     url(r'index^$', views.index, name='index'),





     )


# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )