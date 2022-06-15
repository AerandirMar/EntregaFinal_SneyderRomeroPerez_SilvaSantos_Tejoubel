from django.shortcuts import render
from django.db.models import Q
from accion.models import Accion
from accion.forms import AccionForm
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict


def accions(request):
    '''Creamos la función en views para llamar a Accion (desde models) como un objeto y acumule todo en la variable accions.
    Luego se guarda todo como key & value dentro del diccionario
    '''
    accions = Accion.objects.all()

    context_dict = {
        'accions': accions
    }
    '''Renderizamos para visualizarlo en la url del template_name'''
    return render(
        request=request,
        context=context_dict,
        template_name="accion/accion_lista.html"
    )


@login_required
def accion_forms_django(request):
    if request.method == 'POST':
        accion_form = AccionForm(request.POST)
        '''Mediante "_form.is_valid" se validan los datos, necesario para avanzar por el if'''
        if accion_form.is_valid():
            ''' "_form.cleaned_data" Devuelve un diccionario de campos de entrada de formulario validados y sus valores, 
            donde las claves primarias de cadena se devuelven como objetos'''
            data = accion_form.cleaned_data
            accion = Accion( 
                name=data['name'],
                fecha_estreno=data['fecha_estreno'],
                duracion=data['duracion'],
                sinopsis=data['sinopsis'],                       
            )
            '''Guarda los datos recolectados en BBDD'''
            accion.save()

            '''Los acumula en el dict para renderizarlos posteriormente'''
            accions = Accion.objects.all()
            context_dict = {
                'accions': accions
            }
            return render(
                request=request,
                context=context_dict,
                template_name="accion/accion_lista.html"
            )

    accion_form = AccionForm(request.POST)
    context_dict = {
        'accion_form': accion_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='accion/accion_django_forms.html'
    )


def search(request):
    '''Si no se ingresa ningún valor en los campos, no arroja ningún mensaje'''
    context_dict = dict() 

    '''(text_search) Si encuentra un valor coincidente en el campo "name" dentro de Accion
     de "models" y dentro de la variable "search_param" lo acumula dentro del diccionario
    '''

    '''(fecha_estreno_search) Si encuentra un valor coincidente en el campo "fecha_estreno" dentro de Accion
     de "models" y dentro de la variable "search_param" lo acumula dentro del diccionario
    '''    

    '''(all_search) Si encuentra un valor coincidente en el campo "name" o (OR) "fecha_estreno" dentro de Accion
     de "models" y dentro de la variable "search_param" lo acumula dentro del diccionario
    '''
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        accions = Accion.objects.filter(name__contains=search_param)
        context_dict = {
            'accions': accions
        }

    elif request.GET['fecha_estreno_search']:
        search_param = request.GET['fecha_estreno_search']
        accions = Accion.objects.filter(fecha_estreno__contains=search_param)
        context_dict = {
            'accions': accions
        }
          
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        '''Se utiliza query.add para añadir el resultado de búsqueda al query de name'''
        query.add(Q(fecha_estreno__contains=search_param), Q.OR)

        '''Guarda el resultado en el dict'''
        accions = Accion.objects.filter(query)
        context_dict = {
            'accions': accions
        }
        
    '''Renderiza el resultado de búsqueda en home.html, que es donde se ubica la página de búsqueda'''
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html",
    )


@login_required
def accion_actualiza(request, pk: int):
    accion = Accion.objects.get(pk=pk)

    if request.method == 'POST':
        accion_form = AccionForm(request.POST)
        if accion_form.is_valid():
            data = accion_form.cleaned_data
            accion.name = data['name']
            accion.fecha_estreno = data['fecha_estreno']
            accion.duracion = data['duracion']
            accion.sinopsis = data['sinopsis']
            accion.save()

            accions = Accion.objects.all()
            context_dict = {
                'accions': accions
            }
            return render(
                request=request,
                context=context_dict,
                template_name="accion/accion_lista.html"
            )

    accion_form = AccionForm(model_to_dict(accion))
    context_dict = {
        'accion': accion,
        'accion_form': accion_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='accion/accion_django_forms.html'
    )


@login_required
def borrar_accion(request, pk: int):
    accion = Accion.objects.get(pk=pk)
    if request.method == 'POST':
        accion.delete()

        accions = Accion.objects.all()
        context_dict = {
            'accions': accions
        }
        return render(
            request=request,
            context=context_dict,
            template_name="accion/accion_lista.html"
        )

    context_dict = {
        'accion': accions,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='accion/accion_conf_borrado.html'
    )    