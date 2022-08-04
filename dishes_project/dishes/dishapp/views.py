from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from dishapp.models import Dishes

from dishapp.serializer import DishSerializer

from rest_framework import status


class DishesView(APIView):  # list all products
    def get(self, request, *args, **kwargs):
        qs = Dishes.objects.all()
        # Deserialization
        serializer = DishSerializer(qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):  # create a product
        # Serialization
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            Dishes.objects.create(**serializer.validated_data, status=status.HTTP_200_OK)  # short step
            # Products.objects.create(product_name=request.data.get("product_name"),
            #                         category=request.data.get("category"),                                           # lengthy step
            #                         price=request.data.get("price"),
            #                         rating=request.data.get("rating"))
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DishDetailView(APIView):  # get a specific product
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = Dishes.objects.get(id=id)
        # Deserialization
        serializer = DishSerializer(qs)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        instance = Dishes.objects.filter(id=id)
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            # instance.dish_name=serializer.validated_data.get("dish_name")
            # instance.price=serializer.validated_data.get("price")
            # instance.category=serializer.validated_data.get("category")
            # instance.rating=serializer.validated_data.get("rating")
            #
            # instance.save()
            instance.update(**serializer.validated_data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        instance = Dishes.objects.get(id=id)
        serializer = DishSerializer(instance)
        instance.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)
