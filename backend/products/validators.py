from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from products.models import Product

# def validate_title(value):
#         qs = Product.objects.filter(title__iexact=value)
#         if qs.exists():
#             raise serializers.ValidationError("This product title is already in use.")
#         return value

def validate_title_no_space(value):
    if " " in value:
        raise serializers.ValidationError("Spaces are not permitted in product titles.")
    return value

unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')
