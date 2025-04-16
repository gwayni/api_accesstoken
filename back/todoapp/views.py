from django.shortcuts import render
from rest_framework import viewsets
from .models import items
from .serializer import itemsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class itemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = items.objects.all()
    serializer_class = itemsSerializer

class SecureHelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}!"})


    
