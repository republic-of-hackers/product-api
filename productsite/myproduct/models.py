import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.html import mark_safe
from django.conf import settings

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, name='category', blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField()
    mrp = models.PositiveBigIntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    taxRate = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(50),
            MinValueValidator(1)
        ]
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, name='category', blank=True, null=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, name='subcategory', blank=True, null=True)

    productImage = models.ImageField(upload_to='product-images', default=None)

    def image_tag(self):
        return mark_safe('<img src="%s%s" width="300" height="200" />' % (settings.MEDIA_URL, self.productImage))

    image_tag.short_description = 'Image'

    def _calc_total_price(self):
        if self.mrp and self.taxRate:
            return self.mrp*self.taxRate
        else:
            return "Not Calculated"

    total_price = property(_calc_total_price)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.id)
