from django.db import models

# Create your models here.
# ratings/models.py

from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=100)
    # Add other course fields as needed


class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('course', 'user')