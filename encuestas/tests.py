from django.test import TestCase
from .models import Encuesta, Pregunta, Opcion

class EncuestaModelTest(TestCase):
    def setUp(self):
        self.encuesta = Encuesta.objects.create(titulo="Test Encuesta")
        self.pregunta = Pregunta.objects.create(encuesta=self.encuesta, texto="Pregunta test")
        self.opcion1 = Opcion.objects.create(pregunta=self.pregunta, texto="Opcion A")
        self.opcion2 = Opcion.objects.create(pregunta=self.pregunta, texto="Opcion B")

    def test_creacion_encuesta(self):
        self.assertEqual(self.encuesta.titulo, "Test Encuesta")
        self.assertEqual(self.pregunta.encuesta, self.encuesta)
        self.assertEqual(self.opcion1.pregunta, self.pregunta)
        self.assertEqual(self.opcion1.votos, 0)

    def test_votar_opcion(self):
        self.opcion1.votos += 1
        self.opcion1.save()
        self.assertEqual(self.opcion1.votos, 1)

