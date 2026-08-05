from django.contrib import admin

from profiles.models import JobSeekerProfile,EmployerProfile

# Register your models here.
admin.site.register(JobSeekerProfile)
admin.site.register(EmployerProfile)