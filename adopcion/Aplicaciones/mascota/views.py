from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Persona, Mascota, Adopcion
from django.db.models import Count
from django.utils import timezone
from django.http import HttpResponseBadRequest



# Vista principal (home)
def home(request):
    return render(request, 'mascotas/home.html')


# --- PERSONA ---

def listar_personas(request):
    personas = Persona.objects.all()
    return render(request, 'mascotas/listar_personas.html', {'personas': personas})

def crear_persona(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        cedula = request.POST.get('cedula')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        if not (nombre and apellido and cedula):
            messages.error(request, 'Nombre, Apellido y Cédula son obligatorios.')
            return redirect('crear_persona')

        Persona.objects.create(
            nombre=nombre,
            apellido=apellido,
            cedula=cedula,
            telefono=telefono,
            direccion=direccion
        )
        messages.success(request, 'Persona creada exitosamente.')
        return redirect('listar_personas')

    return render(request, 'mascotas/crear_persona.html')

def editar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if request.method == 'POST':
        persona.nombre = request.POST.get('nombre')
        persona.apellido = request.POST.get('apellido')
        persona.cedula = request.POST.get('cedula')
        persona.telefono = request.POST.get('telefono')
        persona.direccion = request.POST.get('direccion')
        persona.save()
        messages.success(request, 'Persona actualizada exitosamente.')
        return redirect('listar_personas')
    return render(request, 'mascotas/editar_persona.html', {'persona': persona})

def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    persona.delete()
    messages.success(request, 'Persona eliminada correctamente.')
    return redirect('listar_personas')


# --- MASCOTA ---

def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/listar_mascotas.html', {'mascotas': mascotas})

def crear_mascota(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        raza = request.POST.get('raza')
        sexo = request.POST.get('sexo')
        fecha_ingreso = request.POST.get('fecha_ingreso')
        estado = request.POST.get('estado')
        observaciones = request.POST.get('observaciones')

        if not (nombre and tipo and fecha_ingreso):
            messages.error(request, 'Nombre, Tipo y Fecha de Ingreso son obligatorios.')
            return redirect('crear_mascota')

        Mascota.objects.create(
            nombre=nombre,
            tipo=tipo,
            raza=raza,
            sexo=sexo,
            fecha_ingreso=fecha_ingreso,
            estado=estado,
            observaciones=observaciones
        )
        messages.success(request, 'Mascota creada exitosamente.')
        return redirect('listar_mascotas')

    return render(request, 'mascotas/crear_mascota.html')

def editar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    if request.method == 'POST':
        mascota.nombre = request.POST.get('nombre')
        mascota.tipo = request.POST.get('tipo')
        mascota.raza = request.POST.get('raza')
        mascota.sexo = request.POST.get('sexo')
        mascota.fecha_ingreso = request.POST.get('fecha_ingreso')
        mascota.estado = request.POST.get('estado')
        mascota.observaciones = request.POST.get('observaciones')
        mascota.save()
        messages.success(request, 'Mascota actualizada exitosamente.')
        return redirect('listar_mascotas')
    return render(request, 'mascotas/editar_mascota.html', {'mascota': mascota})

def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    mascota.delete()
    messages.success(request, 'Mascota eliminada correctamente.')
    return redirect('listar_mascotas')




def listar_adopciones(request):
    adopciones = Adopcion.objects.select_related('persona', 'mascota').all()
    return render(request, 'mascotas/listar_adopciones.html', {'adopciones': adopciones})

def crear_adopcion(request):
    personas = Persona.objects.all()
    mascotas = Mascota.objects.filter(estado='disponible')
    if request.method == 'POST':
        persona_id = request.POST.get('persona')
        mascota_id = request.POST.get('mascota')
        fecha_adopcion = request.POST.get('fecha_adopcion')
        observaciones = request.POST.get('observaciones')
        
        if not (persona_id and mascota_id and fecha_adopcion):
            messages.error(request, 'Debe seleccionar Persona, Mascota y Fecha de Adopción.')
            return redirect('crear_adopcion')
       

        persona = get_object_or_404(Persona, id=persona_id)
        mascota = get_object_or_404(Mascota, id=mascota_id)

        Adopcion.objects.create(
            persona=persona,
            mascota=mascota,
            fecha_adopcion=fecha_adopcion,
            observaciones=observaciones
        )
        # Opcional: cambiar estado de la mascota a no disponible
        mascota.estado = 'no_disponible'
        mascota.save()

        messages.success(request, 'Adopción registrada exitosamente.')
        return redirect('listar_adopciones')

    return render(request, 'mascotas/crear_adopcion.html', {
        'personas': personas,
        'mascotas': mascotas,
    })

aaaa
    
    if request.method == 'POST':
        persona_id = request.POST.get('persona')
        mascota_id = request.POST.get('mascota')
        fecha_adopcion = request.POST.get('fecha_adopcion')
        observaciones = request.POST.get('observaciones')
        
        if not (persona_id and mascota_id and fecha_adopcion):
            messages.error(request, 'Debe seleccionar Persona, Mascota y Fecha de Adopción.')
            return redirect('editar_adopcion', id=id)
        
        persona = get_object_or_404(Persona, id=persona_id)
        mascota = get_object_or_404(Mascota, id=mascota_id)
        
        adopcion.persona = persona
        adopcion.mascota = mascota
        adopcion.fecha_adopcion = fecha_adopcion
        adopcion.observaciones = observaciones
        adopcion.save()
        
        messages.success(request, 'Adopción actualizada exitosamente.')
        return redirect('listar_adopciones')
    
    return render(request, 'mascotas/editar_adopcion.html', {
        'adopcion': adopcion,
        'personas': personas,
        'mascotas': mascotas,
    })

def eliminar_adopcion(request, id):
    adopcion = get_object_or_404(Adopcion, id=id)
    mascota = adopcion.mascota
    mascota.estado = 'disponible'
    mascota.save()
    adopcion.delete()
    messages.success(request, 'Adopción eliminada correctamente.')
    return redirect('listar_adopciones')
# ---- Vista para reportes de adopciones ----
def reportes_adopciones(request):
    """
    Genera datos para gráficos: agrupa por mascota__tipo y cuenta adopciones (COUNT).
    Soporta filtros GET: filtro = todo|dia|mes|anio   y top = 5|10|20|50|100|all
    URL ejemplo: /adopciones/reportes/?filtro=mes&top=10
    """
    filtro = request.GET.get('filtro', 'todo')
    top = request.GET.get('top', '10')

    # Query base
    qs = Adopcion.objects.select_related('mascota').all()

    # Filtrado por fecha según 'filtro' (usa fecha_adopcion)
    hoy = timezone.localdate()
    if filtro == 'dia':
        qs = qs.filter(fecha_adopcion=hoy)
    elif filtro == 'mes':
        qs = qs.filter(fecha_adopcion__year=hoy.year, fecha_adopcion__month=hoy.month)
    elif filtro == 'anio':
        qs = qs.filter(fecha_adopcion__year=hoy.year)
    elif filtro == 'todo':
        pass
    else:
        # si el filtro no es válido, devolvemos bad request (opcional)
        return HttpResponseBadRequest("Filtro inválido")

    # Agrupar por mascota__tipo y contar adopciones
    agrupamiento = 'mascota__tipo'
    resultados = (
        qs
        .values(agrupamiento)
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    # Aplicar top (si top != 'all')
    if top != 'all':
        try:
            top_n = int(top)
            if top_n > 0:
                resultados = resultados[:top_n]
        except ValueError:
            # si no es convertible a int ni 'all', usar 10 por defecto
            resultados = resultados[:10]

    # Preparar listas para Chart.js
    chart_labels = [item.get(agrupamiento) or 'Sin tipo' for item in resultados]
    chart_data = [item.get('total', 0) for item in resultados]

    context = {
        'chart_labels': chart_labels,
        'chart_data': chart_data,
        'filtro': filtro,
        'top': top,
    }

    return render(request, 'mascotas/reportes_adopciones.html', context)


def grafico_adopciones(request):
    # Datos simulados (puedes reemplazar con datos de tu modelo)
    animales = ['Gato', 'Perro', 'Conejo']
    adopciones = [3, 5, 2]

    # Crear figura más grande
    plt.figure(figsize=(8, 6))
    plt.bar(animales, adopciones, color=['#1e88e5', '#43a047', '#f4511e'])

    # Configurar eje Y para que empiece en 0
    plt.ylim(bottom=0)
    plt.xlabel('Tipo de mascota')
    plt.ylabel('Número de adopciones')
    plt.title('Cantidad de adopciones por tipo de mascota')

    # Guardar gráfico en memoria
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Convertir a base64 para enviar al HTML
    grafico_base64 = base64.b64encode(image_png).decode('utf-8')

    # Renderizar plantilla
    return render(request, 'mascotas/grafico.html', {'grafico_base64': grafico_base64})
