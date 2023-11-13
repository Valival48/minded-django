
from django.contrib import admin
from django.urls import path
from MindED import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signin,name='index'),
    path('index/',views.signin,name='index'),
    path('registro/',views.registro,name='registro'),   
    path('paciente/',views.pacientes,name='paciente'), 
    path('historial/',views.historial,name='historial'),
    path('historial/<int:paciente_id>/',views.sesiones,name='sesiones'),
    path('historial/<int:paciente_id>/intervencion/<int:intervencion_id>/', views.intervencion_detail, name='intervencion_detail'),
    path('test/',views.encuesta_view,name='encuesta_view'),     
    path('inicio/',views.inicio,name='inicio'),
    path('paciente/add/',views.create_paciente,name='create_paciente'),
    path('paciente/<int:paciente_id>/', views.paciente_detail,name='paciente_detail'),
    path('logout/',views.signout,name='logout'),
    path('buscar-pacientes/', views.buscar_pacientes, name='buscar_pacientes') 
]

