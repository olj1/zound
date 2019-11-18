from django.urls import path, include
from .views import CedictionaryViewSet # This library gives us all of the functions usually found in views.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cedictionary', CedictionaryViewSet, basename='cedictionary')
urlpatterns = router.urls