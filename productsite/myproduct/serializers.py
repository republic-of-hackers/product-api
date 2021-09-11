from rest_framework import serializers
from . import models
import base64
from django.conf import settings
import os

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ['id', 'name']

class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SubCategory
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ['id', 'name', 'description', 'mrp', 'taxRate', 'total_price', 'category', 'subcategory', 'productImage']
