from rest_framework import serializers
from .models import ChatHistory

class ChatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatHistory
        fields = ['id', 'user', 'chat_message', 'system_answer', 'timestamp', 'is_from_system', 'descriptions']
        read_only_fields = ['timestamp']