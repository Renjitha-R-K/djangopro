from .models import EmployerProfile,JobSeekerProfile


def profile_status(request):
    if request.user.is_authenticated:
       has_jobseeker_profile=JobSeekerProfile.objects.filter(user=request.user).exists()
       has_employer_profile=EmployerProfile.objects.filter(user=request.user).exists()

       return{
            "has_jobseeker_profile":has_jobseeker_profile,
            "has_employer_profile":has_employer_profile
        }


    return {
            "has_jobseeker_profile":False,
            "has+employer_profile":False


    }
