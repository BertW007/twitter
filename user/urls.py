from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^login/$', views.UserLoginView.as_view(), name='user-login'),
    url(r'^logout/', views.UserLogoutView.as_view(), name='user-logout'),
    url(r'^register/$', views.UserCreateView.as_view(), name='user-create'),
    url(r'^account/edit/(?P<pk>(\d)+)/$', views.UserEditView.as_view(), name='user-edit'),

]