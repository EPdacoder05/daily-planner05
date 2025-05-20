from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class WeeklyPlanner(models.Model):
    TASK_STATUS = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
        ('Deleted', 'Deleted')
    ]
    
    TASK_TYPES = [
        ('home', 'Home'),
        ('work', 'Work'),
        ('leisure', 'Leisure')
    ]
    
    TIME_RANGE_CHOICES = [
        ('morning', 'Morning (6AM-12PM)'),
        ('afternoon', 'Afternoon (12PM-5PM)'),
        ('evening', 'Evening (5PM-10PM)')
    ]
    
    RECURRENCE_CHOICES = [
        ('one_time', 'One Time'),
        ('recurring', 'Recurring')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_priority = models.BooleanField(default=False)
    task_title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    notes = models.TextField(blank=True) #Space for additional context 
    status = models.CharField(max_length=50, choices=TASK_STATUS)
    type_of_task = models.CharField(max_length=50, choices=TASK_TYPES)
    week_start_date = models.DateField(default=timezone.now)
    week_end_date = models.DateField() 
    time_range = models.CharField(max_length=10, choices=TIME_RANGE_CHOICES)
    time_block = models.CharField(max_length=50)
    specific_time = models.TimeField()
    is_recurring = models.CharField(max_length=10, choices=RECURRENCE_CHOICES)
   
    def __str__(self):
        priority_marker = "!" if self.is_priority else ""
        display_status = "Completed" if self.status == 'completed' else "In Progress"
        time_info = f" ({self.specific_time.strftime('%H:%M')})" if self.time_range else ""
        recurrence_info = " (Recurring)" if self.is_recurring == 'recurring' else ""
        task_type_info = f" - {self.get_task_type_display()}" if self.type_of_task else ""
        return f"{self.task_title} {priority_marker} - {display_status()}{time_info}{recurrence_info}{task_type_info}"


class DailyPlanner(models.Model):
    date = models.DateField(default=timezone.now)
    time_range = models.CharField(max_length=10, choices=WeeklyPlanner.TIME_RANGE_CHOICES)
    time_block = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_priority = models.BooleanField(default=False)
    task_title = models.CharField(max_length=250)
    type_of_type = models.CharField(max_length=50)
    specific_time = models.TimeField()
    status = models.CharField(max_length=50, choices=WeeklyPlanner.TASK_STATUS)
    is_recurring = models.CharField(max_length=10, choices=WeeklyPlanner.RECURRENCE_CHOICES)

    def __str__(self):
        priority_marker = "!" if self.is_priority else ""
        display_status = "Completed" if self.status == 'completed' else "In Progress"
        time_info = f" ({self.specific_time.strftime('%H:%M')})" if self.time_range else ""
        recurrence_info = " (Recurring)" if self.is_recurring == 'recurring' else ""
        task_type_info = f" - {self.get_task_type_display()}" if self.type_of_task else ""
        return f"{self.task_title} {priority_marker} - {display_status()}{time_info}{recurrence_info}{task_type_info}"
    class Meta:
        ordering = ['-is_priority', 'date', 'specific_time']