from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from dishapp.models import Dishes
from dishapp.serializers import ProductsSerializer

class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.