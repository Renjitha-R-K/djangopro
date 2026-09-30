"""
URL configuration for careerhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import JobListAPIView,JobDetailAPIView,ApplyJobAPIView

urlpatterns = [
    path('jobs/',JobListAPIView.as_view(),name='job-list-api'),
    path('jobs/<int:pk>/',JobDetailAPIView.as_view(), name='job-detail-api'),
    path('apply/<int:pk>/',ApplyJobAPIView.as_view(),name='apply-job-api'),

]