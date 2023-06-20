from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


def index(request):
    return render(request, "index.html")



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter,]
    search_fields = ['title', 'description',]

    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['products',]

    search_fields = ['positions__product__title', 'positions__product__description',]

    # при необходимости добавьте параметры фильтрации
