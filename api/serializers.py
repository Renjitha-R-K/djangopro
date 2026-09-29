from rest_framework import serializers

from jobs.models import Job



class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model= Job
        fields=['id','title','job_type','description','location','salary','requirements','deadline']