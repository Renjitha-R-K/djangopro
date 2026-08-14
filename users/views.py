from django.shortcuts import render, redirect

from django.views import View

from users.forms import CustomUserForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')


class RegisterView(View):
    def get(self,request):
        form_instance=CustomUserForm()
        return render(request,'register.html',{'forms':form_instance})
    def post(self,request):
        form_instance=CustomUserForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:login')
        return render(request, 'registration.html', {'forms': form_instance})



