from rest_framework import serializers
from .models import Planner  # Replace 'YourModel' with your actual model name

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planner
        fields = '__all__'