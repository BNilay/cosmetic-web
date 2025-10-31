from django.contrib import admin
from django.urls import path,include
from nbeauty.views import home
from django.contrib.auth import views as auth_views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

   path('admin/', admin.site.urls),
path("nbeauty/",include('nbeauty.urls')),
 path("", include("django.contrib.auth.urls")), 
 

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)