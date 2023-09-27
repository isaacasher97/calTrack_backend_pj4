from.models import Food
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import FoodSerializer, UserSerializer, GroupSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class FoodViewSet(viewsets.ModelViewSet):
    #Main query for the index route
    queryset = Food.objects.all()
    #serializer class for serializing output
    serializer_class = FoodSerializer
    #permission class to set permission level
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

class UserViewSet(viewsets.ModelViewSet):
    #Main query for the index route
    queryset = User.objects.all()
    #serializer class for serializing output
    serializer_class = UserSerializer
    #permission class to set permission level
    permission_classes = [permissions.AllowAny]

class GroupViewSet(viewsets.ModelViewSet):
    #Main query for the index route
    queryset = Group.objects.all()
    #serializer class for serializing output
    serializer_class = GroupSerializer
    #permission class to set permission level
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (JWTAuthentication,)