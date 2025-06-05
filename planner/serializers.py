from rest_framework import serializers
from .models import WeeklyPlanner, DailyPlanner  # Replace 'YourModel' with your actual model name

class WeeklyPlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyPlanner
        fields = '__all__'

class DailyPlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPlanner
        fields = '__all__'
