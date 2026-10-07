from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from profiles.models import EmployerProfile,JobSeekerProfile
from .models import Job, Application
from .forms import JobForm,ApplicationForm,ApplicationUpdateForm
from django.contrib import messages
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

class JobDetailView(LoginRequiredMixin,View):
    def get(self,request,pk):
        job = get_object_or_404(Job, pk=pk)
        already_applied = False
        if request.user.role == 'job_seeker':
            if JobSeekerProfile.objects.filter(user=request.user).exists():
                job_seeker=JobSeekerProfile.objects.get(user=request.user)
                if Application.objects.filter(job_seeker=job_seeker,job=job).exists():
                    already_applied=True
        return render(request,'detail.html',{'job':job,'already_applied':already_applied})


class JobListView(LoginRequiredMixin,View):
    def get(self,request):
        if request.user.role != 'job_seeker':
            return redirect('users:home')
        jobs=Job.objects.filter(is_active=True)
        locations=Job.objects.filter(is_active=True).values_list('location',flat=True).distinct()
        data=request.GET.get('q')
        selected_location = request.GET.get('location')
        selected_job_type=request.GET.get('job_type')
        job_types=Job._meta.get_field('job_type').choices
        if selected_location:
            jobs = jobs.filter(location=selected_location)
        if selected_job_type:
            jobs = jobs.filter(job_type=selected_job_type)
        if data:
            jobs = jobs.filter(Q(title__icontains=data))
        paginator=Paginator(jobs,8)
        page_number = request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        job_seeker=JobSeekerProfile.objects.get(user=request.user)
        applied_job_ids=Application.objects.filter(job_seeker=job_seeker).values_list('job_id',flat=True)
        return render(request,'joblist.html',{'jobs':page_obj,'locations':locations,'selected_location':selected_location,'job_types': job_types,'selected_job_type':selected_job_type,'applied_job_ids':applied_job_ids})


class ApplyJobView(LoginRequiredMixin,View):
    def get(self,request,pk):
        if request.user.role != 'job_seeker':
            return redirect('users:home')

        job=Job.objects.get(pk=pk)
        form_instance = ApplicationForm()
        return render(request,'apply.html',{'job':job,'form':form_instance})


    def post(self,request,pk):
        if request.user.role != 'job_seeker':
            return redirect('users:home')

        if JobSeekerProfile.objects.filter(user=request.user).exists():
            form_instance=ApplicationForm(request.POST,request.FILES)

            job = get_object_or_404(Job, pk=pk)
            if form_instance.is_valid():
                apply=form_instance.save(commit=False)
                jobseeker_profile=JobSeekerProfile.objects.get(user=request.user)
                apply.job=job
                apply.job_seeker=jobseeker_profile
                if Application.objects.filter(job_seeker=jobseeker_profile,job=job).exists():
                    messages.warning(request, "You have already applied for this job.")
                    return redirect('jobs:job-detail',pk=pk)
                apply.save()
                messages.success(request,"Application submitted successfully!")
                return redirect('jobs:job-detail', pk=pk)
            return render(request, 'apply.html', {'job': job, 'form': form_instance})
        return redirect('profiles:create-jobseeker-profile')



class MyApplicationsView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role != 'job_seeker':
            return redirect('users:home')
        if JobSeekerProfile.objects.filter(user=request.user).exists():
            jobseeker_profile=JobSeekerProfile.objects.get(user=request.user)
            applications=Application.objects.filter(job_seeker=jobseeker_profile)
            return render(request,'applyview.html',{'applications': applications})
        return redirect('profiles:create-jobseeker-profile')


class ViewApplicationsView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role != 'employer':
            return redirect('users:home')

        if EmployerProfile.objects.filter(user=request.user).exists():
            employer_profile=EmployerProfile.objects.get(user=request.user)
            applications=Application.objects.filter(job__employer=employer_profile)
            return render(request,'viewapply.html',{'applications':applications})
        return redirect('profiles:create-employer-profile')


class ApplicationDetailView(LoginRequiredMixin,View):
    def get(self,request,pk):
        if request.user.role!= 'employer':
            return redirect('users:home')

        if EmployerProfile.objects.filter(user=request.user).exists():
            employer_profile = EmployerProfile.objects.get(user=request.user)
            application=get_object_or_404(Application.objects.filter(job__employer=employer_profile),pk=pk)
            return render(request,'appdetail.html',{'application':application})
        return redirect('profiles:create-employer-profile')


class ApplicationUpdateView(LoginRequiredMixin,View):
    def get(self,request,pk):
        if request.user.role != 'employer':
            return redirect('users:home')
        if EmployerProfile.objects.filter(user=request.user).exists():
            employer_profile=EmployerProfile.objects.get(user=request.user)
            application=get_object_or_404(Application.objects.filter(job__employer=employer_profile),pk=pk)
            form_instance=ApplicationUpdateForm(instance=application)
            return render(request,'appupdate.html',{'form':form_instance})
        return redirect('profiles:create-employer-profile')


    def post(self,request,pk):
        if request.user.role != 'employer':
            return redirect('users:home')
        if EmployerProfile.objects.filter(user=request.user).exists():
            employer_profile = EmployerProfile.objects.get(user=request.user)
            application = get_object_or_404(Application.objects.filter(job__employer=employer_profile), pk=pk)
            form_instance = ApplicationUpdateForm(request.POST,instance=application)
            if form_instance.is_valid():
                form_instance.save()
                return redirect('jobs:view-applications')
            return render(request, 'appupdate.html', {'form': form_instance})
        return redirect('profiles:create-employer-profile')



class EditJobView(LoginRequiredMixin,View):
    def get(self,request,pk):
        if request.user.role != 'employer':
            return redirect('users:home')
        if EmployerProfile.objects.filter(user=request.user).exists():
            emp = EmployerProfile.objects.get(user=request.user)
            job=get_object_or_404(Job,employer=emp,id=pk)
            form_instance=JobForm(instance=job)
            return render(request,'editjob.html',{'form':form_instance})
        return redirect('profiles:create-employer-profile')
    def post(self,request,pk):
        if request.user.role != 'employer':
            return redirect('users:home')
        if EmployerProfile.objects.filter(user=request.user).exists():
            emp=EmployerProfile.objects.get(user=request.user)
            job=get_object_or_404(Job,employer=emp,id=pk)
            form_instance=JobForm(request.POST,instance=job)
            if form_instance.is_valid():
                form_instance.save()
                return redirect('jobs:my-jobs')
            return render(request,'editjob.html',{'form':form_instance})
        return redirect('profiles:create-employer-profile')





class DeleteJobView(LoginRequiredMixin,View):
    def get(self,request,pk):
        if request.user.role != 'employer':
            return redirect('users:home')
        if EmployerProfile.objects.filter(user=request.user).exists():
            emp=EmployerProfile.objects.get(user=request.user)
            job=get_object_or_404(Job,employer=emp,id=pk)
            return render(request,'deletejob.html',{'job':job})
        return redirect('profiles:create-employer-profile')

    def post(self,request,pk):
        if request.user.role != 'employer':
            return redirect('users:home')
        if EmployerProfile.objects.filter(user=request.user).exists():
            emp=EmployerProfile.objects.get(user=request.user)
            job=get_object_or_404(Job,employer=emp,id=pk)
            job.delete()
            return redirect('jobs:my-jobs')
        return redirect('profiles:create-employer-profile')




class EmployerDashboardView(LoginRequiredMixin, View):
    def get(self, request):
         if request.user.role != 'employer':
             return redirect('users:home')
         if EmployerProfile.objects.filter(user=request.user).exists():
             emp=EmployerProfile.objects.get(user=request.user)
             jobs=Job.objects.filter(employer=emp)
             total_jobs=jobs.count()
             active_jobs=jobs.filter(is_active=True).count()
             applications = Application.objects.filter(job__employer=emp)
             total_applications=applications.count()
             recent_applications=applications.order_by('-applied_date')[:5]
             return render(request,'empdashboard.html',{'total_jobs':total_jobs,'active_jobs':active_jobs,'total_applications':total_applications,'recent_applications':recent_applications})
         return redirect('users:home')


class JobSeekerDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role !="job_seeker":
            return redirect('users:home')
        if JobSeekerProfile.objects.filter(user=request.user).exists():
            jobseeker=JobSeekerProfile.objects.get(user=request.user)
            applications=Application.objects.filter(job_seeker=jobseeker)
            total_applications=applications.count()
            applied = applications.filter(status='applied').count()
            shortlisted=applications.filter(status='shortlisted').count()
            rejected=applications.filter(status='rejected').count()
            hired=applications.filter(status='hired').count()
            recent_applications=applications.order_by('-applied_date')[:5]
            return render(request,'jobseekerdashboard.html',{'total_applications':total_applications,'applied':applied,'shortlisted':shortlisted,'rejected':rejected,'hired':hired,'recent_applications':recent_applications})
        return redirect('users:home')