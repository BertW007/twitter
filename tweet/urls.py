from django.conf.urls import url

from tweet import views

urlpatterns = [
    url(r'^$', views.TweetListView.as_view(), name='tweet-list'),
    url(r'^tweet/detail/(?P<pk>(\d)+)$', views.TweetDetailView.as_view(), name='tweet-detail'),
    url(r'^tweet/create/$', views.TweetCreateView.as_view(), name='tweet-create'),
    url(r'^user/(?P<username>[^/]+)/tweet/$', views.UserTweetListView.as_view(), name='user-tweet-list'),
]