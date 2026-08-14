from django.shortcuts import render,redirect

from profiles.models import EmployerProfile
from .models import Job
from .forms import JobForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class CreateJobView(LoginRequiredMixin,View):
    def get(self, request):
        if request.user.role != 'employer':
            return redirect('users:home')

        if EmployerProfile.objects.filter(user=request.user).exists():
            form_instance = JobForm()
            return render(request,'createjob.html',{'form': form_instance})



        return redirect('users:home')

    def post(self,request):
        if request.user.role != 'employer':
            return redirect('users:home')

        if EmployerProfile.objects.filter(user=request.user).exists():
            form_instance=JobForm(request.POST)
            if form_instance.is_valid():
                job=form_instance.save(commit=False)
                employer_profile=EmployerProfile.objects.get(user=request.user)
                job.employer=employer_profile
                job.save()
                return redirect('users:home')
            return render(request, 'createjob.html', {'form': form_instance})
        return redirect('users:home')




class MyJobsView(LoginRequiredMixin,View):
    def get(self,request):
        if request.user.role != 'employer':
            return redirect('users:home')
        if EmployerProfile.objects.filter(user=request.user).exists():
            employer_profile=EmployerProfile.objects.get(user=request.user)
            jobs=Job.objects.filter(employer=employer_profile)

            return render(request,'myjobs.html',{'jobs':jobs})
        return redirect('users:home')