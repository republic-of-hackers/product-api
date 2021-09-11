from django.contrib import admin
from .models import Product, Category, SubCategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    fields = ["name", "category"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # fields = ["name", "description", ("mrp", "taxRate", ), ("category", "subcategory")]
    display_list = ["name", "description","mrp", "taxRate","category", "subcategory","total_price" ,'image_tag']
    readonly_fields = ["total_price", 'image_tag']
