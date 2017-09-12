from django.conf.urls import url

from message import views

urlpatterns = [
    url(r'^account/(?P<pk>(\d)+)/message/create/$', views.MessageCreateView.as_view(), name='message-create'),
    url(r'^account/(?P<pk>(\d)+)/message/list/$', views.MessageReceiverListView.as_view(), name='message-receiver-list'),
]