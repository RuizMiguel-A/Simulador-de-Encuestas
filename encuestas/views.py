from django.shortcuts import render, get_object_or_404, redirect
from .models import Encuesta, Pregunta, Opcion, Respuesta 

def home(request):
    encuestas = Encuesta.objects.all()
    return render(request, 'encuestas/home.html', {'encuestas': encuestas})

def responder_encuesta(request, encuesta_id):
    encuesta = get_object_or_404(Encuesta, pk=encuesta_id)
    preguntas = encuesta.preguntas.all()

    if request.method == 'POST':
        for pregunta in preguntas:
            opcion_id = request.POST.get(f'pregunta_{pregunta.id}')
            if opcion_id:
                opcion = get_object_or_404(Opcion, pk=opcion_id)
                Respuesta.objects.create(pregunta=pregunta, opcion=opcion)
                opcion.votos += 1  
                opcion.save()
request, 'encuestas/responder.html', {'encuesta': encuesta, 'preguntas': preguntas})

def resultados_encuesta(request, encuesta_id):
    encuesta = get_object_or_404(Encuesta, pk=encuesta_id)
    preguntas = encuesta.preguntas.all()

    resultados = []
    for pregunta in preguntas:
        opciones = pregunta.opciones.all()
        total = sum(o.votos for o in opciones)
        porcentajes = {
            opcion.texto: (opcion.votos / total * 100) if total > 0 else 0
            for opcion in opciones
        }
        resultados.append({
            'pregunta': pregunta,
            'porcentajes': porcentajes,
        })

    return render(request, 'encuestas/resultados.html', {'encuesta': encuesta, 'resultados': resultados})
