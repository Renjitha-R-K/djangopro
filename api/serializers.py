from rest_framework import serializers

from jobs.models import Job,Application



class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model= Job
        read_only_fields=['id']
        fields=['id','title','job_type','description','location','salary','requirements','deadline','is_active']



class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        read_only_fields=['job','employer_note','status','updated_at']
        fields=['job','resume','cover_letter','status','updated_at','employer_note']








