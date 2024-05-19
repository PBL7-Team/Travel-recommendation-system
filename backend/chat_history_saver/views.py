from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import ChatHistory
from .serializers import ChatHistorySerializer
# from django.http import HttpResponse
from rest_framework.response import Response

class ChatHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = ChatHistorySerializer
    #permission_classes = [permissions.AllowAny]

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):       
        # try:
        return ChatHistory.objects.filter(user=self.request.user).order_by('-timestamp')
        # except Exception as e:
        #     # Handle the exception or log it if necessary
        #     # return HttpResponse("User not found", status=404)
        #     return None

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def list(self, request):
        queryset = ChatHistory.objects.filter(user=self.request.user).order_by('-timestamp')
        serializer = ChatHistorySerializer(queryset, many=True)
        return Response(serializer.data)

