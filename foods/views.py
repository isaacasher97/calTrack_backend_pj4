from.models import Food
from rest_framework import viewsets, permissions
from .serializers import FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    #Main query for the index route
    queryset = Food.objects.all()
    #serializer class for serializing output
    serializer_class = FoodSerializer
    #permission class to set permission level
    permission_classes = [permissions.AllowAny]