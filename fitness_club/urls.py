from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/clients/', include('clients.urls')),
    path('api/workouts/', include('workouts.urls')),
    path('api/schedule/', include('schedule.urls')),
    path('api/analytics/', include('analytics.urls')),
]
