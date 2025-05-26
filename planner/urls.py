from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'weekly-planner', views.WeeklyPlannerViewSet, basename='weekly-planner')
router.register(r'daily-planner', views.DailyPlannerViewSet, basename='daily-planner')

urlpatterns = [
    
    path('', include(router.urls)),     # path('your-endpoint/', views.YourView.as_view(), name='your-view-name'),
]   