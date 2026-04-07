from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, GroupClassViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'group-classes', GroupClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
