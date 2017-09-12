from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, related_name='user_sender')
    receiver = models.ForeignKey(User, related_name='user_receiver')
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    @property
    def name(self):
        return 'From {} to {}'.format(self.sender, self.receiver)

    def __str__(self):
        return self.name