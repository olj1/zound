from django.urls import path, include
from .views import ProfileViewSet, LanguageViewSet, WordViewSet, ConnectionViewSet 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'profiles', ProfileViewSet, basename='profiles')
router.register(r'languages', LanguageViewSet, basename='languages')
router.register(r'words', WordViewSet, basename='words')
router.register(r'connections', ConnectionViewSet, basename='connections')

urlpatterns = router.urls