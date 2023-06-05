from rest_framework import mixins, viewsets

from products.models import Product
from products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
        GET -> list -> Queryset
        GET -> retrieve -> Product instance (Detail view)
        POST -> create -> New instance
        PUT -> update
        PATCH -> partial update
        DELETE -> destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """
        GET -> list -> Queryset
        GET -> retrieve -> Product instance (Detail view)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'