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
from jobs import views

app_name="jobs"
urlpatterns = [
    path("create/", views.CreateJobView.as_view(), name="create-job"),
    path('my-jobs/',views.MyJobsView.as_view(),name='my-jobs'),
    path('jobs-list/',views.JobListView.as_view(),name='job-list'),
    path('job-apply/<int:pk>/',views.ApplyJobView.as_view(),name='job-apply'),
    path('my-app/',views.MyApplicationsView.as_view(),name='my-app'),
    path('applications/',views.ViewApplicationsView.as_view(),name='view-applications'),
    path('app-detail/<int:pk>/',views.ApplicationDetailView.as_view(),name='app-detail'),
    path('app-update/<int:pk>/',views.ApplicationUpdateView.as_view(),name='app-update'),
    path('editjob/<int:pk>/',views.EditJobView.as_view(),name='editjob'),
    path('deletejob/<int:pk>/',views.DeleteJobView.as_view(),name='deletejob'),
    path('emp-dashboard/', views.EmployerDashboardView.as_view(), name='emp-dashboard'),
    path('jobseek-dashboard/',views.JobSeekerDashboardView.as_view(),name='jobseek-dashboard'),
    path('<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),

]
