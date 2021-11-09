from django.contrib.auth.models import User, Group
from .models import Vehicle, Route, Session, Checkpoint
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class CheckpointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Checkpoint
        fields = "__all__"
