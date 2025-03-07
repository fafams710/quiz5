from django.urls import path
from .views import GetProducts, GetProduct

urlpatterns = [
    path('', GetProducts.as_view(), name='product-list'),
    path('<uuid:uuid>/', GetProduct.as_view(), name='product-detail'),
]
