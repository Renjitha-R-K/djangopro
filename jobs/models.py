

from django.db import models
from profiles.models import EmployerProfile


class Job(models.Model):
    JOB_TYPE_CHOICES=[
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
        ('contract', 'Contract'),
    ]


    employer=models.ForeignKey(EmployerProfile,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    requirements=models.TextField()
    location=models.CharField(max_length=150)
    job_type=models.CharField(max_length=20,choices=JOB_TYPE_CHOICES)
    salary=models.CharField(max_length=100)
    deadline=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title