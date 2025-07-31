from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('<int:encuesta_id>/responder/', views.responder_encuesta, name='responder_encuesta'),
    path('encuesta/<int:encuesta_id>/resultados/', views.resultados_encuesta, name='resultados_encuesta'),

]
