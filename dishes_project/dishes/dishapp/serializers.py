from rest_framework import serializers

class ProductsSerializer(serializers.Serializer):
    product_name=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()