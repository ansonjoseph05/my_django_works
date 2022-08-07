from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from dishapp.models import Dishes

from dishapp.serializer import DishSerializer, DishModelSerializer, UserSerializer

from rest_framework import status

from rest_framework.viewsets import ViewSet, ModelViewSet

from rest_framework import authentication,permissions


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
        id=kwargs.get("id")
        instance=Dishes.objects.filter(id=id)
        serializer=DishSerializer(data=request.data)
        if serializer.is_valid():
            # instance.dish_name=serializer.validated_data.get("dish_name")
            # instance.price=serializer.validated_data.get("price")
            # instance.category=serializer.validated_data.get("category")
            # instance.rating=serializer.validated_data.get("rating")
            # instance.save()
            instance.update(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        instance = Dishes.objects.get(id=id)
        serializer = DishSerializer(instance)
        instance.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)


#  Model Serializer

class DishModelView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Dishes.objects.all()
        if "category" in request.query_params:
            qs = qs.filter(category=request.query_params.get("category"))
        if "price_gt" in request.query_params:
            qs = qs.filter(price_gte=request.query_params.get("price_gt"))
        serializer = DishModelSerializer(qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = DishModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


class DishDetailsModelView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = Dishes.objects.get(id=id)
        serializer = DishModelSerializer(qs)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        object = Dishes.objects.get(id=id)
        serializer = DishModelSerializer(data=request.data, instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        object = Dishes.objects.get(id=id)
        object.delete()
        return Response({"msg:deleted"}, status=status.HTTP_204_NO_CONTENT)


# -------------- ViewSet ---------------


class DishViewSetView(ViewSet):
    def list(self, request, *args, **kwargs):
        qs = Dishes.objects.all()
        serializer = DishModelSerializer(qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        pass

    def create(self, request, *args, **kwargs):
        serializer = DishModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = Dishes.objects.get(id=id)
        serializer = DishModelSerializer(qs)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        object = Dishes.objects.get(id=id)
        serializer = DishModelSerializer(instance=object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        instance = Dishes.objects.get(id=id)
        instance.delete()
        return Response({"msg:deleted"}, status=status.HTTP_204_NO_CONTENT)


class DishModelViewSetView(ModelViewSet):
    serializer_class = DishModelSerializer
    queryset = Dishes.objects.all()
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


from django.contrib.auth.models import User


class UserModelViewSetView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
