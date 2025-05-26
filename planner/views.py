from django.shortcuts import render
from rest_framework import viewsets
from .models import WeeklyPlanner, DailyPlanner
from .serializers import WeeklyPlannerSerializer, DailyPlannerSerializer

class WeeklyPlannerViewSet(viewsets.ModelViewSet):
    queryset = WeeklyPlanner.objects.all()
    serializer_class = WeeklyPlannerSerializer

class DailyPlannerViewSet(viewsets.ModelViewSet):
    queryset = DailyPlanner.objects.all()
    serializer_class = DailyPlannerSerializer
