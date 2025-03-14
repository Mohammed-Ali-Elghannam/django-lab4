from django.db import models
from course_app.models import Course  

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name="trainees")  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

