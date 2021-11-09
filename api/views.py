from django.contrib.auth.models import User, Group
from .models import Vehicle, Route, Checkpoint, Session
from rest_framework import viewsets
from .serializers import CheckpointSerializer, RouteSerializer, SessionSerializer, UserSerializer, GroupSerializer, VehicleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all().order_by("fecha_alta")
    serializer_class = VehicleSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all().order_by("fecha_inicio")
    serializer_class = RouteSerializer


class CheckpointViewSet(viewsets.ModelViewSet):
    queryset = Checkpoint.objects.all().order_by("fecha")
    serializer_class = CheckpointSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by("fecha")
    serializer_class = SessionSerializer
