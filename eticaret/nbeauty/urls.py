from django.urls import path
from . import views

app_name='nbeauty'

urlpatterns = [
    path('',views.home,name='home'), 
    path('routines/',views.routines,name='routines'),

]
