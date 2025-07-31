# crear_encuestas.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "encuesta_beta.settings")
django.setup()

from encuestas.models import Encuesta, Pregunta, Opcion

# Encuesta 1
encuesta1 = Encuesta.objects.create(titulo="Evaluación del Docente")

p1 = Pregunta.objects.create(encuesta=encuesta1, texto="¿Cómo calificarías al docente?")
for texto in ["Excelente", "Buena", "Regular", "Mala"]:
    Opcion.objects.create(pregunta=p1, texto=texto)

p2 = Pregunta.objects.create(encuesta=encuesta1, texto="¿Fue claro al explicar?")
for texto in ["Siempre", "A veces", "Nunca"]:
    Opcion.objects.create(pregunta=p2, texto=texto)

# Encuesta 2
encuesta2 = Encuesta.objects.create(titulo="Opinión sobre el Curso")

p3 = Pregunta.objects.create(encuesta=encuesta2, texto="¿Recomendarías este curso?")
for texto in ["Sí", "No"]:
    Opcion.objects.create(pregunta=p3, texto=texto)

print("Encuestas creadas correctamente.")
