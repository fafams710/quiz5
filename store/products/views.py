from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser  # Added import
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404

class GetProducts(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class GetProduct(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, uuid):
        product = get_object_or_404(Product, uuid=uuid)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
