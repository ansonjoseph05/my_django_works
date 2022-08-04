from django.shortcuts import render

# Create your views here.

from menu.models import menu_items

from rest_framework.views import APIView
from rest_framework.response import Response


class MenuView(APIView):
    def get(self, request, *args, **kwargs):
        all_items = menu_items
        if "category" in request.query_params:
            category = request.query_params.get("category")
            all_items = [item for item in menu_items if item.get("category") == category]
        if "limit" in request.query_params:
            lim = int(request.query_params.get("limit"))
            all_items = all_items[:lim]

        return Response(data=all_items)

    def post(self, request, *args, **kwargs):
        data = request.data
        menu_items.append(data)
        return Response(data=menu_items)


class MenuDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        pid = kwargs.get("pid")
        menu = [items for items in menu_items if items.get("code") == pid].pop()
        return Response(data=menu)

    def put(self, request, *args, **kwargs):
        pid = kwargs.get("pid")
        data = [items for items in menu_items if items.get("code") == pid].pop()
        menu_items.update(request.data)
        return Response(data=menu_items)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("pid")
        instance = [item for item in menu_items if item.get("code") == id].pop()
        menu_items.remove(instance)
        return Response(data=menu_items)

