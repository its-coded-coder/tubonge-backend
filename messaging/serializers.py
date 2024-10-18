
from rest_framework import serializers
from .models import Message, ConferenceRoom

class ConferenceRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceRoom
        fields = ('id', 'name', 'host', 'participants', 'created_at')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'content', 'timestamp')
