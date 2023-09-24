from .models import Food
from rest_framework import serializers

#Food Serializer
class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'calories', 'fat', 'protein', 'carbs', 'sugar']