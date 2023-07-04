# views.py
from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .mypaginations import MyPageNumberPagination

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAdminUser]
 
 
    filterset_fields = ['name']
    filter_backends = [DjangoFilterBackend]
 
    pagination_class = MyPageNumberPagination
    #pagination_class = PageNumberPagination

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAdminUser]
 
 
    filterset_fields = ['name']
    filter_backends = [DjangoFilterBackend]
 
    pagination_class = MyPageNumberPagination
    #pagination_class = PageNumberPagination

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAdminUser]
 
 
    filterset_fields = ['name']
    filter_backends = [DjangoFilterBackend]
 
    pagination_class = MyPageNumberPagination
    #pagination_class = PageNumberPagination

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAdminUser]
 
 
    filterset_fields = ['name']
    filter_backends = [DjangoFilterBackend]
 
    pagination_class = MyPageNumberPagination
    #pagination_class = PageNumberPagination
