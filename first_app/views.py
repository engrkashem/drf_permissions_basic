from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from . import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import ProductPagination, ProductLimitOffsetPagination, ProductCursorPagination

# Create your views here.


class ProductViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated | permissions.ReadOnly]
    # permission_classes = [IsAdminUser | permissions.ReadOnly]
    # permission_classes = [permissions.AdminOrReadOnly]
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['name', 'description']
    # ordering_fields = ['price']
    # pagination_class = ProductPagination
    # pagination_class = ProductLimitOffsetPagination

    # for cursor pagination filtering should be stopped
    pagination_class = ProductCursorPagination


class ProductReviewViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.ReviewOrReadOnly]
    queryset = models.ProductReviewModel.objects.all()
    serializer_class = serializers.ProductReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'rating']

    # def get_queryset(self):
    #     queryset = models.ProductReviewModel.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains=username)
    #     return queryset
