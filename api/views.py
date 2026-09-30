
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from jobs.models import Job,Application
from profiles.models import EmployerProfile,JobSeekerProfile
from .serializers import JobSerializer,ApplicationSerializer
from .permissions import IsEmployer, IsJobOwner,IsJobSeeker


class JobListAPIView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [IsEmployer()]
        else:
            permission_classes=[IsAuthenticated()]
        return permission_classes
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
    def get_permissions(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            permission_classes = [IsEmployer(), IsJobOwner()]
        else:
            permission_classes = [IsAuthenticated()]
        return permission_classes
    def get(self, request, pk):
        job=get_object_or_404(Job,pk=pk)
        serializer=JobSerializer(job)
        return Response(serializer.data)
    def put(self,request,pk):
        job=get_object_or_404(Job,pk=pk)
        self.check_object_permissions(request,job)
        serializer=JobSerializer(job,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        job=get_object_or_404(Job,pk=pk)
        self.check_object_permissions(request, job)
        serializer=JobSerializer(job,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        job=get_object_or_404(Job,pk=pk)
        self.check_object_permissions(request, job)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ApplyJobAPIView(APIView):
    permission_classes = [IsJobSeeker]
    def post(self,request,pk):
        job=get_object_or_404(Job,pk=pk)
        jobseek=JobSeekerProfile.objects.get(user=request.user)
        apply=Application.objects.filter(job=job,job_seeker=jobseek)
        if apply.exists():
            return Response({"detail": "You have already applied for this job."}, status=status.HTTP_409_CONFLICT)
        serializer=ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(job=job,job_seeker=jobseek)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class MyApplicationsAPIView(APIView):
    permission_classes = [IsJobSeeker]
    def get(self,request):
        jobseek=JobSeekerProfile.objects.get(user=request.user)
        apply=Application.objects.filter(job_seeker=jobseek,)
        serializer=ApplicationSerializer(apply,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

