from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('mysite.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'my_homepage_view'),
    url(r'^join/$', 'join'),
    url(r'^joinform/$', 'joinform'),
    url(r'^register/$', 'registerform'),
    url(r'^login/$', 'loginform'),
    url(r'^home/$', 'homeform'),
    url(r'^toregister/$', 'register'),
    url(r'^tologin/$', 'login'),
    url(r'^index/$', 'index'),
    url(r'^joindetail/$', 'joindetail'),
    url(r'^contactus/$', 'contactus'),
)