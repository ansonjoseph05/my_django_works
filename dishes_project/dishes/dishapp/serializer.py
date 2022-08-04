from rest_framework import serializers
from dishapp.models import Dishes
class DishSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    dish_name=serializers.CharField()
    price = serializers.IntegerField()
    category=serializers.CharField()
    rating=serializers.FloatField()

    def validate(self,data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("invalid price")
        return data

class DishModelSerializer(serializers.ModelSerializer):
    model=Dishes
    # fields=["dish_name",
    #         "price",
    #         "category",
    #         "rating"]

    #   OR

    fields="__all__"

