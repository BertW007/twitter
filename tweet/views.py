from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from tweet.forms import UserTweetCreateForm
from tweet.models import Tweet


class TweetListView(ListView):
    model = Tweet
    template_name = 'tweet/tweet_list.html'

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.filter(user=int(self.kwargs['pk']))
    #     return qs

class TweetDetailView(View):

    def get(self, request, pk):
        user = User.objects.filter(pk=pk)
        tweet = Tweet.objects.filter(user=user)
        return render(request, 'tweet/tweet_detail.html', {
            'tweet': tweet,
            'user': user,
        })


class UserTweetListView(ListView):
    # model = Tweet
    # template_name = 'tweet/user_tweet_list.html'
    #
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.filter(user=self.request.user)
    #     return qs
    def get(self, request, username):
        user = User.objects.get(username=username)
        user_tweet = Tweet.objects.filter(user=user)
        return render(request, 'tweet/user_tweet_list.html', {
            'user': user,
            'user_tweet': user_tweet,
        })


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    form_class = UserTweetCreateForm
    template_name = 'tweet/tweet_create_form.html'
    success_url = reverse_lazy('tweet-list')
    raise_exception = True
    # def hande_no_permission(self):
    #     if self.request.user.is_authenticated and self.raise_exception:  # jezeli jestes zalogowany i nie masz uprwanien, 403
    #         return HttpResponseForbidden()
    #     else:
    #         return redirect(settings.LOGIN_URL)
    #
    # def get_success_url(self):
    #     return reverse('user-tweet-list', kwargs={
    #         'pk': self.object.user.id,
    #     })

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

