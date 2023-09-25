from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from . import permissions

# Create your views here.


class ProductViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated | permissions.ReadOnly]
    # permission_classes = [IsAdminUser | permissions.ReadOnly]
    permission_classes = [permissions.AdminOrReadOnly]
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductReviewViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.ReviewOrReadOnly]
    queryset = models.ProductReviewModel.objects.all()
    serializer_class = serializers.ProductReviewSerializer
