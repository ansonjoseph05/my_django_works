from rest_framework import serializers
from productsapi.models import Products
from django.contrib.auth.models import User

class ProductSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    product_name=serializers.CharField()
    price=serializers.IntegerField()
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
            raise serializers.ValidationError("invalid rating")
        return data


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=[
            "id",
            "product_name",
            "price",
            "category",
            "rating"
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields=[
            "username",
            "first_name",
            "last_name",
            "email",
            "password"
        ]                                  # we dont use "__all__" here