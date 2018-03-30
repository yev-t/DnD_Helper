from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="log_in"),
	url(r'^register$', views.register_user, name="register_user"),
	url(r'^login$', views.login_user, name="login_user"),
	url(r'^home$', views.home, name="my_home"),
	url(r'^logout$', views.logout, name="logout"),
	url(r'^delete$', views.delete_user, name="delete"),
]