from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
import requests


# Create your views here.
class MyAPIView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, action):
        if action == "start-crawl":
            return self.start_crawl()
        elif action == "sentiment-calculate":
            return self.sentiment_calculate()
        elif action == "get-crawl-info":
            return self.get_crawl_info()
        elif action == "stop-crawl":
            return self.stop_crawl()
        else:
            return Response(
                {"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST
            )

    def start_crawl(self):
        url = "http://flask-app.southeastasia.cloudapp.azure.com:8080/start-crawl"
        headers = {"API-Key": "PBL_7_Traveling"}
        try:
            response = requests.get(url, headers=headers)
            result = response.json()
            return Response(result, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as err:
            return Response(
                {"message": f"Error occurred: {err}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except ValueError as json_err:
            return Response(
                {"message": "Invalid JSON response"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def stop_crawl(self):
        url = "http://flask-app.southeastasia.cloudapp.azure.com:8080/stop-crawl"
        headers = {"API-Key": "PBL_7_Traveling"}
        try:
            response = requests.get(url, headers=headers)
            result = response.json()
            return Response(result, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as err:
            return Response(
                {"message": f"Error occurred: {err}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except ValueError as json_err:
            return Response(
                {"message": "Invalid JSON response"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def sentiment_calculate(self):
        url = (
            "http://flask-app.southeastasia.cloudapp.azure.com:8080/sentiment-caculate"
        )
        headers = {"API-Key": "PBL_7_Traveling"}
        try:
            response = requests.get(url, headers=headers)
            result = response.json()
            return Response(result, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as err:
            return Response(
                {"message": f"Error occurred: {err}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except ValueError as json_err:
            return Response(
                {"message": "Invalid JSON response"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def get_crawl_info(self):
        url = "http://flask-app.southeastasia.cloudapp.azure.com:8080/get-crawl-info"
        headers = {"API-Key": "PBL_7_Traveling"}
        try:
            response = requests.get(url, headers=headers)
            result = response.json()
            return Response(result, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as err:
            return Response(
                {"message": f"Error occurred: {err}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except ValueError as json_err:
            return Response(
                {"message": "Invalid JSON response"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
