from django.contrib.auth.models import User, Group
from .models import ModelVehiculo
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, VehicleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = ModelVehiculo.objects.all()
    serializer_class = VehicleSerializer
