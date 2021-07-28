from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('welcome',views.welcome),
    path('login', views.login),
    path('addjob',views.addjob),
    path('delete',views.delete_job),
    path('logout',views.logout),
    path('jobs',views.jobs),
    path('jobs/edit/<int:num>', views.job_edit_page),
    path('editjob/<int:num>', views.editjob),
    path('profile',views.profile_page)
]