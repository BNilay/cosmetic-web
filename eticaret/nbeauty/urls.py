from django.urls import path
from . import views
from .views import SignUpView

app_name='nbeauty'

urlpatterns = [
    path('',views.home,name='home'), 
    path('routines/',views.routines,name='routines'),
    path('cleanser/',views.cleanser,name='cleanser'),
    path('moisturizer/',views.moisturizer,name='moisturizer'),
    path('serum/',views.serum,name='serum'),
    path('toner/',views.toner,name='toner'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
   

]
