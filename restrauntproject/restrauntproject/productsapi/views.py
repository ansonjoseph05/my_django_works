from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from productsapi.models import Products
from productsapi.serializer import ProductSerializer, ProductModelSerializer
from rest_framework import status
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.contrib.auth.models import User

class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Products.objects.all()
        # Desirialization
        serializer = ProductSerializer(qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Serialization
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            Products.objects.create(**serializer.validated_data)
            # Products.objects.create(product_name=serializer.validated_data.get("product_name"),
            #                         price=serializer.validated_data.get("price"),
            #                         category=serializer.validated_data.get("category"),
            #                         rating=serializer.validated_data.get("rating"))

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        instance = Products.objects.get(id=id)
        # Deserialization
        serializer = ProductSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        instance = Products.objects.filter(id=id)
        # Serialization
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            instance.update(**serializer.validated_data, )
            # instance.product_name=serializer.validated_data.get("product_name")
            # instance.price=serializer.validated_data.get("price")
            # instance.category=serializer.validated_data.get("category")
            # instance.rating=serializer.validated_data.get("rating")
            # instance.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        instance = Products.objects.get(id=id)
        instance.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)


# ------------------ Model Serializer ---------------------


class ProductModelView(APIView):

    def get(self, request, *args, **kwargs):
        # Deserialization
        qs = Products.objects.all()
        serializer = ProductModelSerializer(qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        # Serialization
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # we use save() because ModelSerializer has inbuilt create() function
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailModelView(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        instance = Products.objects.get(id=id)
        # Deserialization
        serializer = ProductModelSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):

        id = kwargs.get("id")
        object = Products.objects.get(id=id)
        # Serialization
        serializer = ProductModelSerializer(data=request.data, instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):

        id = kwargs.get("id")
        instance = Products.objects.get(id=id)
        instance.remove()
        return Response({"msg": "deleted"})


# -------------- ViewSet -------------

class ProductViewSetView(ViewSet):
    def list(self, request, *args, **kwargs):
        qs = Products.objects.all()
        serializer = ProductModelSerializer(qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance = Products.objects.get(id=id)
        serializer = ProductModelSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        object = Products.objects.get(id=id)
        serializer = ProductModelSerializer(data=request.data, instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance = Products.objects.get(id=id)
        instance.delete()
        return Response({"msg":"Deleted"},status=status.HTTP_204_NO_CONTENT)

class ProductModelViewSetView(ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = Products.objects.all()


class UserModelViewSetView(ModelViewSet):
    serializer_class = User
    queryset = User.objects.all()