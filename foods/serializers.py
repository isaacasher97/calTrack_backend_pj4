from .models import Food
from rest_framework import serializers
from django.contrib.auth.models import User, Group

#Food Serializer
class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'calories', 'fat', 'protein', 'carbs', 'sugar']

#User Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']