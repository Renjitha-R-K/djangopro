from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from jobs.models import Job
from profiles.models import EmployerProfile
from .serializers import JobSerializer

class JobListAPIView(APIView):
    def get(self,request):
        jobs=Job.objects.all()
        serializer=JobSerializer(jobs,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=JobSerializer(data=request.data)
        if serializer.is_valid():
            employer = EmployerProfile.objects.get(user=request.user)
            serializer.save(employer=employer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class JobDetailAPIView(APIView):
    def get(self, request, pk):
        job=get_object_or_404(Job,pk=pk)
        serializer=JobSerializer(job)
        return Response(serializer.data)