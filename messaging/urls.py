
from django.urls import path
from .views import SendMessageView, MessageHistoryView, CreateConferenceRoomView, JoinConferenceRoomView

urlpatterns = [
    path('send/', SendMessageView.as_view(), name='send_message'),
    path('history/', MessageHistoryView.as_view(), name='message_history'),
    path('create-room/', CreateConferenceRoomView.as_view(), name='create_room'),
    path('join-room/<int:pk>/', JoinConferenceRoomView.as_view(), name='join_room'),
]
