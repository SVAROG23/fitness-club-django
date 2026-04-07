from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as users_views
from workouts import views as workouts_views
from analytics import views as analytics_views
from schedule import views as schedule_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', users_views.dashboard, name='dashboard'),
    
    # API endpoints
    path('api/users/', include('users.urls')),
    path('api/clients/', include('clients.urls')),
    path('api/workouts/', include('workouts.urls')),
    path('api/schedule/', include('schedule.urls')),
    path('api/analytics/', include('analytics.urls')),
    
    # Views
    path('clients/', clients_views.client_list, name='client_list'),
    path('clients/<int:client_id>/', clients_views.client_detail, name='client_detail'),
    path('workouts/', workouts_views.program_list, name='program_list'),
    path('workouts/<int:program_id>/', workouts_views.program_detail, name='program_detail'),
    path('workouts/fix/<int:workout_id>/', workouts_views.workout_fix, name='workout_fix'),
    path('schedule/', schedule_views.calendar, name='calendar'),
    path('reports/', analytics_views.reports, name='reports'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
