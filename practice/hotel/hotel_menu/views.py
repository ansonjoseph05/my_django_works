from django.shortcuts import render

# Create your views here.

from restrauntproject.models import menu_items

from rest_framework.views import APIView
from rest_framework.response import Response


class MenuView(APIView):
    def get(self,request,*args,**kwargs):
        if "limit" in request.query_params:
            data=int(request.query_params.get("limit"))
            menu=[for item in menu_items if item.get("code")]
        return Response(data=menu_items)

class MenuDetailsViews(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        data=[item for item in menu_items if item.get("code")==pid].pop()
        return Response(data=data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("pid")
        instance=[item for item in menu_items if item.get("code")==id].pop()
        data=request.data
        instance.update(data)
        return Response(data=data)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pid")
        instance=[item for item in menu_items if item.get("code")==id].pop()
        menu_items.remove(instance)
        return Response(data=menu_items)
