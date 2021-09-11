from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'subcategory', views.SubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]