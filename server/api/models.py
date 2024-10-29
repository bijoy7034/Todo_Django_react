from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    category = models.CharField(max_length=100, blank=True, null=True)
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='Medium')
    progress_percentage = models.IntegerField(default=0) 
    def __str__(self):
        return self.title