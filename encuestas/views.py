from django.shortcuts import render, get_object_or_404, redirect
from .models import Encuesta, Pregunta, Opcion, Respuesta
from .forms import EncuestaForm, PreguntaForm
from django.forms import inlineformset_factory

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
        return redirect('resultados_encuesta', encuesta_id=encuesta.id)

    return render(request, 'encuestas/responder.html', {'encuesta': encuesta, 'preguntas': preguntas})

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

OpcionFormSet = inlineformset_factory(Pregunta, Opcion, fields=['texto'], extra=1, max_num=4)


#función para crear una encuesta
def crear_encuesta(request):
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        pregunta_form = PreguntaForm(request.POST)
        
        # Validar ambos formularios antes de crear el formset
        if form.is_valid() and pregunta_form.is_valid():
            # Guarda la encuesta y la pregunta solo si ambos formularios son válidos
            encuesta = form.save()
            pregunta = pregunta_form.save(commit=False)
            pregunta.encuesta = encuesta
            pregunta.save()

            # Crea una instancia del formset de opciones con la instancia de la pregunta
            formset = OpcionFormSet(request.POST, instance=pregunta)

            if formset.is_valid():
                # Guarda el formset de opciones y redirige
                formset.save()
                return redirect('home')
        
        # Si alguno de los formularios no es válido, renderiza la plantilla con los errores
        else:
            formset = OpcionFormSet(request.POST, instance=pregunta_form.instance if pregunta_form.is_valid() else None)
            return render(request, 'encuestas/crear_encuesta.html', {'form': form, 'pregunta_form': pregunta_form, 'formset': formset})

    else:
        # En una petición GET, se crean los formularios vacíos
        form = EncuestaForm()
        pregunta_form = PreguntaForm()
        formset = OpcionFormSet()

    return render(request, 'encuestas/crear_encuesta.html', {'form': form, 'pregunta_form': pregunta_form, 'formset': formset})
