
from django.contrib import admin
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.Register.as_view()),
    url(r'^register$', views.Register.as_view()),
    url(r'^login/$', views.Login.as_view()),
    url(r'^login$', views.Login.as_view()),
    url(r'^$', views.home),
    url(r'^succ/$', views.home),
    url(r'^logout$', views.Logout.as_view())
]
