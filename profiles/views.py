from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import JobSeekerProfileForm,EmployerProfileForm
from .models import JobSeekerProfile,EmployerProfile

class CreateJobSeekerProfileView(LoginRequiredMixin,View):
    def get(self,request):
        if JobSeekerProfile.objects.filter(user=request.user).exists():
            return redirect('users:home')

        form_instance=JobSeekerProfileForm()
        return render(request,'jobseeker.html',{'form':form_instance})

    def post(self,request):
        if JobSeekerProfile.objects.filter(user=request.user).exists():
            return redirect("users:home")

        form_instance=JobSeekerProfileForm(request.POST,request.FILES)
        if form_instance.is_valid():
            profile=form_instance.save(commit=False)
            profile.user=request.user
            profile.save()
            return redirect('users:home')
        return render(request, 'jobseeker.html', {'form': form_instance})


class CreateEmployerProfileView(LoginRequiredMixin, View):
    def get(self,request):
        if EmployerProfile.objects.filter(user=request.user).exists():
            return redirect('users:home')
        form_instance=EmployerProfileForm()
        return render(request,'employer.html',{'form':form_instance})

    def post(self,request):
        if EmployerProfile.objects.filter(user=request.user).exists():
            return redirect('users:home')

        form_instance=EmployerProfileForm(request.POST,request.FILES)
        if form_instance.is_valid():
            profile=form_instance.save(commit=False)
            profile.user=request.user
            profile.save()
            return redirect('users:home')
        return render(request, 'employer.html', {'form': form_instance})


class EmployerProfileView(LoginRequiredMixin, View):
    def get(self,request):
        if request.user.role != 'employer':
            return redirect('users:home')

        if EmployerProfile.objects.filter(user=request.user).exists():
            employer=EmployerProfile.objects.get(user=request.user)
            return render(request,'empprofile.html',{'employer':employer})
        return redirect('users:create-employer-profile')


class EditEmployerProfileView(LoginRequiredMixin,View):
    def get(self,request):
        if request.user.role != 'employer':
            return redirect('users:home')
        if EmployerProfile.objects.filter(user=request.user).exists():
           emp=EmployerProfile.objects.get(user=request.user)
           form_instance=EmployerProfileForm(instance=emp)
           return render(request,'editempprofile.html',{'form':form_instance})
        return redirect('profiles:create-employer-profile')


    def post(self,request):
        if request.user.role != 'employer':
            return redirect('users:home')

        if EmployerProfile.objects.filter(user=request.user).exists():
           emp=EmployerProfile.objects.get(user=request.user)
           form_instance=EmployerProfileForm(request.POST,request.FILES,instance=emp)
           if form_instance.is_valid():
               form_instance.save()
               return redirect('profiles:employer-profile')
           return render(request,'editempprofile.html',{'form':form_instance})
        return redirect('profiles:create-employer-profile')



class JobSeekerProfileView(LoginRequiredMixin, View):
    def get(self,request):
        if request.user.role != 'job_seeker':
            return redirect('users:home')
        if JobSeekerProfile.objects.filter(user=request.user).exists():
            jobseeker=JobSeekerProfile.objects.get(user=request.user)
            return render(request,'jobseekerprofile.html',{'jobseeker':jobseeker})
        return redirect('profiles:create-jobseeker-profile')


class EditJobseekerProfileView(LoginRequiredMixin,View):
    def get(self,request):
        if request.user.role != 'job_seeker':
            return redirect('users:home')
        if JobSeekerProfile.objects.filter(user=request.user).exists():
            jobseek=JobSeekerProfile.objects.get(user=request.user)
            form_instance=JobSeekerProfileForm(instance=jobseek)
            return render(request,'editjobseek.html',{'form':form_instance})

    def post(self,request):
        if request.user.role != 'job_seeker':
            return redirect('users:home')

        if JobSeekerProfile.objects.filter(user=request.user).exists():
            jobseek=JobSeekerProfile.objects.get(user=request.user)
            form_instance=JobSeekerProfileForm(request.POST,request.FILES,instance=jobseek)
            if form_instance.is_valid():
                form_instance.save()
                return redirect('profiles:jobseeker-profile')
            return render(request,'editjobseek.html',{'form':form_instance})
        return redirect('profiles:create-jobseeker-profile')

