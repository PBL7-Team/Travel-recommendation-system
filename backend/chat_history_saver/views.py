from django.shortcuts import render
from rest_framework.decorators import action
# Create your views here.
from rest_framework import viewsets, permissions
import rest_framework.decorators

from chat_history_saver.services.contact_rasa import call_rasa
from .models import ChatHistory
from .serializers import ChatHistorySerializer
# from django.http import HttpResponse
from rest_framework.response import Response
from django.http import JsonResponse
import requests

class ChatHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = ChatHistorySerializer
    permission_classes = [permissions.AllowAny]

    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):       
        # try:
        return ChatHistory.objects.filter(user=self.request.user).order_by('-timestamp')
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
        
    def list(self, request):
        queryset = ChatHistory.objects.filter(user=self.request.user).order_by('-timestamp')
        serializer = ChatHistorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        user = self.request.user
        chat_message = serializer.validated_data.get('chat_message')
        url = 'http://rasa-server:5005/webhooks/rest/webhook'  # Replace with your webhook URL

        try:
            response_data = call_rasa(user.username, chat_message, url)
            print('res',response_data)
            system_answer = response_data[0].get('text')
            print('sys',system_answer)
            serializer.save(system_answer=system_answer)
            return JsonResponse({
                'data': response_data,
            }, status=200)
        except requests.exceptions.RequestException as e:
            return JsonResponse({
                'error': 'Failed to call webhook',
                'details': str(e)
            }, status=500)

        
    
    @action(detail=False, methods=['post'], url_path="contact_message")
    def contact(self, request, *args, **kwargs):
        data = {
            'title': 'foo',
            'body': 'bar',
            'userId': 1
        }
        
        # Make a POST request to the external API
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
        
        # Process the response from the API
        if response.status_code == 201:
            response_data = response.json()
            message = "Post created successfully"
        else:
            response_data = {}
            message = "Failed to create post"
        
        # Return the message as a JSON response
        return JsonResponse({
            'message': message,
            'response_data': response_data
        })


    @action(detail=False, methods=['post'], url_path="send_message")
    def send_message(self, request, *args, **kwargs):
        sender = request.data.get('sender')
        message = request.data.get('message')
        url = 'https://example.com/webhook'  # Replace with your webhook URL
        
        try:
            response_data = call_rasa(sender, message, url)
            return JsonResponse({
                'message': 'Webhook called successfully',
                'response_data': response_data
            })
        except requests.exceptions.RequestException as e:
            return JsonResponse({
                'error': 'Failed to call webhook',
                'details': str(e)
            }, status=500)