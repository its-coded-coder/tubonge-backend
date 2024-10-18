
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Message, ConferenceRoom
from .serializers import MessageSerializer, ConferenceRoomSerializer

class CreateConferenceRoomView(generics.CreateAPIView):
    queryset = ConferenceRoom.objects.all()
    serializer_class = ConferenceRoomSerializer

class JoinConferenceRoomView(generics.UpdateAPIView):
    queryset = ConferenceRoom.objects.all()
    serializer_class = ConferenceRoomSerializer

    def update(self, request, *args, **kwargs):
        room = self.get_object()
        room.participants.add(request.user)
        room.save()
        return Response({'status': 'participant added'}, status=status.HTTP_200_OK)

class SendMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

from rest_framework.permissions import IsAuthenticated

class MessageHistoryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)
