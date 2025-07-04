from rest_framework.views import APIView
from rest_framework import generics

from . import models, serializers


class UsersAPIView(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
