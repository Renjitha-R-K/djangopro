
from django.db import models
from django.conf import settings

# Create your models here.



class JobSeekerProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    location=models.CharField(max_length=50)
    skills = models.TextField()
    education=models.CharField(max_length=100)
    experience=models.CharField(max_length=20)
    profile_picture=models.ImageField(upload_to="profiles/",null=True, blank=True)
    resume=models.FileField(upload_to="resumes/",null=True,blank=True)
    github=models.URLField(null=True,blank=True)
    linkedin=models.URLField(null=True,blank=True)


    def __str__(self):
        return self.full_name


class EmployerProfile(models.Model):

    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100)
    company_description=models.TextField()
    website=models.URLField(null=True,blank=True)
    location=models.CharField(max_length=100)
    industry=models.CharField(max_length=80)
    company_logo=models.ImageField(upload_to="employers/",null=True,blank=True)
    company_size=models.CharField(max_length=80,null=True,blank=True)

    def __str__(self):
        return self.company_name

