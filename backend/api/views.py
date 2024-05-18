from django.shortcuts import render
# Create your views here.

from django.http import JsonResponse


def api_data(request):
    # Dummy data for demonstration
    print("Hello, this is test API using Django!", flush=True)
    data = {
        'message': 'Hello, this is my first API using Django!',
        'status': 'success'
    }
    return JsonResponse(data)