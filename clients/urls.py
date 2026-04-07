from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientProfileViewSet, AnthropometryViewSet

router = DefaultRouter()
router.register(r'profiles', ClientProfileViewSet)
router.register(r'anthropometry', AnthropometryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
