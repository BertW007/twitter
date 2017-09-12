from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView

from message.forms import MessageCreateForm
from message.models import Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'message/message_create_form.html'
    raise_exception = True

    # def get(self, request, pk):
    #     User.objects.filter(pk=pk)
    #     return render(request, 'message/message_create_form.html', {
    #         'form': MessageCreateForm(),
    #     })
    #
    # def post(self, request, pk):
    #     form = MessageCreateForm(data=request.POST)
    #     sender = User.objects.filter(pk=pk)
    #     if form.is_valid():
    #         receiver = User.objects.filter(username=form.cleaned_data['receiver'])
    #         Message.objects.create(content=form.cleaned_data['content'], sender_id=sender, receiver=receiver)
    #         return redirect(receiver)
    #     else:
    #         return render(request, 'message/message_create_form.html', {
    #             'form': form,
    #         })
    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.receiver = User.objects.get(pk=self.kwargs['pk'])
        message.save()
        return HttpResponseRedirect(reverse('message-receiver-list', kwargs={
            'pk': int(self.kwargs['pk'])
        }))

class MessageReceiverListView(PermissionRequiredMixin, ListView):
    # def get(self, request, username):
    #     user = User.objects.get(username=username)
    #     message = Message.objects.filter(receiver=username)
    #     return render(request, 'message/message_receiver_list.html', {
    #         'user': user,
    #         'message': message,
    #     })
    model = Message
    template_name = 'message/message_receiver_list.html'
    permission_required = 'message.list_message'
    raise_exception = True

    def hande_no_permission(self):
        if self.request.user.is_authenticated and self.raise_exception: # jezeli jestes zalogowany i nie masz uprwanien, 403
            return HttpResponseForbidden()
        else:
            return redirect(settings.LOGIN_URL)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(receiver=int(self.kwargs['pk']))
        return qs
