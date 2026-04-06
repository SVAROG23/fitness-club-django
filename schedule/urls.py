from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InjuryIncidentViewSet

router = DefaultRouter()
router.register(r'incidents', InjuryIncidentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
