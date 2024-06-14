from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser
import rest_framework.permissions
from rest_framework.response import Response
from django.http import JsonResponse

from destinations.pagination import LargeResultsSetPagination
from .models import Attraction
from .serializers import AttractionSerializer
import json
import requests
from rest_framework import viewsets, permissions
from django.db.models import Sum

class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = LargeResultsSetPagination

    @action(detail=False, methods=["post"], parser_classes=[FileUploadParser])
    def load_from_file(self, request):
        file_obj = request.data["file"]
        if not file_obj.name.endswith(".json"):
            return Response(
                {"error": "File format not supported. Please upload a .json file."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            data = json.load(file_obj)
            for item in data:
                serializer = AttractionSerializer(data=item)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(
                        serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )
            return Response(
                {"status": "Data loaded successfully"}, status=status.HTTP_201_CREATED
            )
        except json.JSONDecodeError:
            return Response(
                {"error": "Invalid JSON file"}, status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=["get"], url_path="fetch-and-save")
    def fetch_and_save_attraction(self, request):
        url = (
            "http://flask-app.southeastasia.cloudapp.azure.com:8080/get-crawl-calc-info"
        )
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                for attraction_data in data:
                    attraction_data_mapped = {
                        "attraction_name": attraction_data.get("attraction_name"),
                        "reviews_count": attraction_data.get("review_count"),
                        "summary": attraction_data.get("attraction_summary"),
                        "general_info": attraction_data,
                        "review_count_non_calc": attraction_data.get(
                            "review_count_non_calc"
                        ),
                    }

                    serializer = AttractionSerializer(data=attraction_data_mapped)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(
                            serializer.errors, status=status.HTTP_400_BAD_REQUEST
                        )

                return Response(
                    {"status": "Attractions saved successfully"},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"error": "Invalid data format from external API"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except requests.RequestException as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Tính tổng các trường review_count và review_count_non_calc
        total_reviews = (
            queryset.aggregate(total_reviews=Sum("reviews_count"))["total_reviews"] or 0
        )
        total_raw_reviews = (
            queryset.aggregate(total_raw_reviews=Sum("review_count_non_calc"))[
                "total_raw_reviews"
            ]
            or 0
        )

        # Phân trang dữ liệu
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response_data = {
                "total_reviews": total_reviews,
                "total_raw_reviews": total_raw_reviews,
                "data": serializer.data,
            }
            return self.get_paginated_response(response_data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
