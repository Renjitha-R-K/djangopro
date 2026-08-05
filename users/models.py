from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    ROLE_CHOICES = [('job_seeker', 'Job Seeker'),('employer', 'Employer'),]

    role = models.CharField(max_length=20,choices=ROLE_CHOICES)