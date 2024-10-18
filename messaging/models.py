
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver} at {self.timestamp}'

class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255)
    host = models.ForeignKey(User, related_name='hosted_rooms', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='joined_rooms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
