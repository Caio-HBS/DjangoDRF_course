import json

from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product 
from products.serializers import ProductSerializer



@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
        DRF API view.
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance  = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({'error': 'invalid data'}, status=400)
