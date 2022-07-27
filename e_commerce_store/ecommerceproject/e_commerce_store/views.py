from django.shortcuts import render

# Create your views here.

from e_commerce_store.models import products

from rest_framework.views import APIView
from rest_framework.response import Response


class ProductsView(APIView):
    def get(self, request, *args, **kwargs):
        if "price_lte" in request.query_params:
            id = int(request.query_params.get("price_lte"))
            data = [product for product in products if product["price"]<=id]
            return Response(data=data)
        return Response(data=products)



    def post(self, request, *args, **kwargs):
        data = request.data
        products.append(data)
        return Response(data=data)


class ProductsViews(APIView):
    def get(self,request,*args,**kwargs):
        if "limit" in request.query_params:
            lim=int(request.query_params.get("limit"))
            data=products
        return Response(data=data[0:lim])