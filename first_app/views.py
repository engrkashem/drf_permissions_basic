from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

# Create your views here.


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ProductViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductReviewViewset(viewsets.ModelViewSet):
    queryset = models.ProductReviewModel.objects.all()
    serializer_class = serializers.ProductReviewSerializer
