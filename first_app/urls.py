from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewset)
router.register('reviews', views.ProductReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
]
