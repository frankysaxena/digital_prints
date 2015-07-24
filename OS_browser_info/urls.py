from django.conf.urls import patterns, url
from OS_browser_info import views

urlpatterns = patterns('',
    url(r'^$', views.hello_runnable, name='hello_runnable'),
)
