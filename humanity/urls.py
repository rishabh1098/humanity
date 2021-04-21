from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('registerasdonar/', include('donar.urls')),
    path('patientregister/', include('patients.urls')),
]