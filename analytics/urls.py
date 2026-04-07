from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InjuryIncidentViewSet, AnalyticsViewSet

router = DefaultRouter()
router.register(r'injuries', InjuryIncidentViewSet)
router.register(r'', AnalyticsViewSet, basename='analytics')

urlpatterns = [
    path('', include(router.urls)),
]
