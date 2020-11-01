from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page 
    path('', views.index, name='home'),

    #The dashboard page
    path('/dashboard', views.dashboard, name='dashboard'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
