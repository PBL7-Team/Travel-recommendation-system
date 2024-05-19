from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Attraction
from .serializers import AttractionSerializer
import json

class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

    @action(detail=False, methods=['post'], parser_classes=[FileUploadParser])
    def load_from_file(self, request):
        file_obj = request.data['file']
        if not file_obj.name.endswith('.json'):
            return Response({"error": "File format not supported. Please upload a .json file."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = json.load(file_obj)
            for item in data:
                serializer = AttractionSerializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"status": "Data loaded successfully"}, status=status.HTTP_201_CREATED)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON file"}, status=status.HTTP_400_BAD_REQUEST)
