from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response

# Create your views here.
class RegisterResource(APIView):
    # pass
    def post(self, request):
        serializer = ResourceSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)