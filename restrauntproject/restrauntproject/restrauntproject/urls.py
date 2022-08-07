"""restrauntproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from menu import views
from rest_framework.routers import DefaultRouter
from productsapi.views import ProductView, ProductDetailsView, ProductModelView, ProductDetailModelView, ProductViewSetView,ProductModelViewSetView,UserModelViewSetView

router = DefaultRouter()
router.register ("api/v3/products", ProductViewSetView, basename="products")
router.register ("api/v4/products", ProductModelViewSetView, basename="mproducts")
router.register ("", UserModelViewSetView ,basename="uprodcuts")


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("hotel/menu/", views.MenuView.as_view()),
                  path("hotel/menu/<int:pid>", views.MenuDetailsView.as_view()),
                  path("myg/products/", ProductView.as_view()),
                  path("myg/products/<int:id>", ProductDetailsView.as_view()),
                  path("api/v2/myg/products/", ProductModelView.as_view()),
                  path("api/v2/myg/products/<int:id>", ProductDetailModelView.as_view())
              ] + router.urls
