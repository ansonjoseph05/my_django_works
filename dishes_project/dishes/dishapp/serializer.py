from rest_framework import serializers
from dishapp.models import Dishes

from django.contrib.auth.models import User
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

    def validate(self,data):
        rating=data.get("rating")
        if rating<0:
            raise serializers.ValidationError("invalid Rating")
        return data

class DishModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        # field=["product_name",
        #        "price",
        #        "category",
        #        "rating"]

        #  OR
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password"
        ]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


