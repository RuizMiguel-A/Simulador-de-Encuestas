#test_views.py
import pytest
from django.urls import reverse
from django.test import Client
from encuestas.models import Encuesta, Pregunta, Opcion

@pytest.mark.django_db
def test_home_view_muestra_encuestas():
    encuesta = Encuesta.objects.create(titulo="¿Te gusta el código?")
    client = Client()
    url = reverse('home')
    response = client.get(url)

    assert response.status_code == 200
    assert '¿Te gusta el código?' in response.content.decode()

@pytest.mark.django_db
def test_responder_encuesta_view():
    encuesta = Encuesta.objects.create(titulo="Encuesta Test")
    pregunta = Pregunta.objects.create(encuesta=encuesta, texto="¿Python o Java?")
    opcion1 = Opcion.objects.create(pregunta=pregunta, texto="Python", votos=0)
    opcion2 = Opcion.objects.create(pregunta=pregunta, texto="Java", votos=0)

    client = Client()
    url = reverse('responder_encuesta', args=[encuesta.id])
    
    # Simulacion de la respuesta a una encuesta
    response = client.post(url, {f'pregunta_{pregunta.id}': opcion1.id})

    # Comprobar redirección
    assert response.status_code == 302  # redirige a resultados
    opcion1.refresh_from_db()
    assert opcion1.votos == 1

@pytest.mark.django_db
def test_resultados_encuesta_view():
    encuesta = Encuesta.objects.create(titulo="Lenguaje favorito")
    pregunta = Pregunta.objects.create(encuesta=encuesta, texto="¿Python o C++?")
    opcion1 = Opcion.objects.create(pregunta=pregunta, texto="Python", votos=3)
    opcion2 = Opcion.objects.create(pregunta=pregunta, texto="C++", votos=1)

    client = Client()
    url = reverse('resultados_encuesta', args=[encuesta.id])
    response = client.get(url)

    assert response.status_code == 200
    assert 'Python' in response.content.decode()
    assert 'C++' in response.content.decode()
