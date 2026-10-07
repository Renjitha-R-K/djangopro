from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View

from users.forms import CustomUserForm


# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')




class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('users:home')

    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully!')
        return super().form_valid(form)

class RegisterView(View):
    def get(self,request):
        form_instance=CustomUserForm()
        return render(request,'register.html',{'forms':form_instance})
    def post(self,request):
        form_instance=CustomUserForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:login')
        return render(request, 'register.html', {'forms': form_instance})


