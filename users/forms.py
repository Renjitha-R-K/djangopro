from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields=['username','email','role','password1','password2']