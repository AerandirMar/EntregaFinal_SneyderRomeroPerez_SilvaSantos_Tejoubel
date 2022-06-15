from django.shortcuts import render
from django.db.models import Q
from drama.models import Drama
from drama.forms import DramaForm
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict


def drama(request):
    '''Creamos la función en views para llamar a Drama (desde models) como un objeto y acumule todo en la variable comedias.
    Luego se guarda todo como key & value dentro del diccionario
    '''
    dramas = Drama.objects.all()

    context_dict = {
            'dramas': dramas
    }
    '''Renderizamos para visualizarlo en la url del template_name'''
    return render(
        request=request,
        context=context_dict,
        template_name="drama/drama_lista.html"
    )


@login_required
def drama_forms_django(request):
    if request.method == 'POST':
        drama_form = DramaForm(request.POST)
        '''Mediante "_form.is_valid" se validan los datos, necesario para avanzar por el if'''
        if drama_form.is_valid():
            ''' "_form.cleaned_data" Devuelve un diccionario de campos de entrada de formulario validados y sus valores, 
            donde las claves primarias de cadena se devuelven como objetos'''
            data = drama_form.cleaned_data
            drama = Drama(
                name=data['name'],
                fecha_estreno=data['fecha_estreno'],
                duracion=data['duracion'],
                sinopsis=data['sinopsis'],
            )

            '''Guarda los datos recolectados en BBDD'''
            drama.save()

            '''Los acumula en el dict para renderizarlos posteriormente'''    
            dramas = Drama.objects.all()
            context_dict = {
                    'dramas': dramas
            }
            return render(
                request=request,
                context=context_dict,
                template_name="drama/drama_lista.html"
            )

    drama_form = DramaForm(request.POST)
    context_dict = {
        'drama_form': drama_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='drama/drama_django_forms.html'
    )


def searchDra(request):
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
        dramas = Drama.objects.filter(name__contains=search_param)
        context_dict = {
            'dramas': dramas
        }

    elif request.GET['fecha_estreno_search']:
        search_param = request.GET['fecha_estreno_search']
        dramas = Drama.objects.filter(fecha_estreno__contains=search_param)
        context_dict = {
            'dramas': dramas
        }

    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        '''Se utiliza query.add para añadir el resultado de búsqueda al query de name'''
        query.add(Q(fecha_estreno__contains=search_param), Q.OR)

        '''Guarda el resultado en el dict'''
        dramas = Drama.objects.filter(query)
        context_dict = {
            'dramas': dramas
        }
    '''Renderiza el resultado de búsqueda en home.html, que es donde se ubica la página de búsqueda'''    
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html",
    )    


@login_required
def drama_actualiza(request, pk: int):
    drama = Drama.objects.get(pk=pk)

    if request.method == 'POST':
        drama_form = DramaForm(request.POST)
        if drama_form.is_valid():
            data = drama_form.cleaned_data
            drama.name = data['name']
            drama.fecha_estreno = data['fecha_estreno']
            drama.duracion = data['duracion']
            drama.sinopsis = data['sinopsis']
            drama.save()

            dramas = Drama.objects.all()
            context_dict = {
                'dramas': dramas
            }
            return render(
                request=request,
                context=context_dict,
                template_name="drama/drama_lista.html"
            )

    drama_form = DramaForm(model_to_dict(drama))
    context_dict = {
        'drama': drama,
        'drama_form': drama_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='drama/drama_django_forms.html'
    )


@login_required
def borrar_drama(request, pk: int):
    drama = Drama.objects.get(pk=pk)
    if request.method == 'POST':
        drama.delete()

        dramas = Drama.objects.all()
        context_dict = {
            'dramas': dramas
        }
        return render(
            request=request,
            context=context_dict,
            template_name="drama/drama_lista.html"
        )

    context_dict = {
        'drama': drama,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='drama/drama_conf_borrado.html'
    )    