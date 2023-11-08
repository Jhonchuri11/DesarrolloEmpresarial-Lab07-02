from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
     path('', views.MatriculaView.as_view(), name='index'),
     path('editarMatricula/<id>/', views.MatriculaView.modificarMatricula, name='editarMatricula')
]

