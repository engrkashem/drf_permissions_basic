from rest_framework import serializers
from .models import ProductModel, ProductReviewModel


class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True)

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReviewModel
        fields = '__all__'
