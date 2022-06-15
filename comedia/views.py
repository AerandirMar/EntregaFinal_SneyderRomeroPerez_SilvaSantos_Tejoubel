from django.shortcuts import render
from django.db.models import Q
from comedia.models import Comedia
from comedia.forms import ComediaForm
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict


def comedias(request):
    '''Creamos la función en views para llamar a Comedia (desde models) como un objeto y acumule todo en la variable comedias.
    Luego se guarda todo como key & value dentro del diccionario
    '''
    comedias = Comedia.objects.all()

    context_dict = {
        'comedias': comedias
    }
    '''Renderizamos para visualizarlo en la url del template_name'''
    return render(
        request=request,
        context=context_dict,
        template_name="comedia/comedia_lista.html"
    )


@login_required
def comedia_forms_django(request):
    if request.method == 'POST':
        comedia_form = ComediaForm(request.POST)
        '''Mediante "_form.is_valid" se validan los datos, necesario para avanzar por el if'''
        if comedia_form.is_valid():
            ''' "_form.cleaned_data" Devuelve un diccionario de campos de entrada de formulario validados y sus valores, 
            donde las claves primarias de cadena se devuelven como objetos'''
            data = comedia_form.cleaned_data
            comedia = Comedia(
                name=data['name'],
                fecha_estreno=data['fecha_estreno'],
                duracion=data['duracion'],
                sinopsis=data['sinopsis'],
            )
            '''Guarda los datos recolectados en BBDD'''
            comedia.save()

            '''Los acumula en el dict para renderizarlos posteriormente'''
            comedias = Comedia.objects.all()
            context_dict = {
                'comedias': comedias
            }
            return render(
                request=request,
                context=context_dict,
                template_name="comedia/comedia_lista.html"
            )

    comedia_form = ComediaForm(request.POST)
    context_dict = {
        'comedia_form': comedia_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='comedia/comedia_django_forms.html'
    )


def searchCom(request):
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
        comedias = Comedia.objects.filter(name__contains=search_param)
        context_dict = {
            'comedias': comedias
        }

    elif request.GET['fecha_estreno_search']:
        search_param = request.GET['fecha_estreno_search']
        comedias = Comedia.objects.filter(fecha_estreno__contains=search_param)
        context_dict = {
            'comedias': comedias
        }

    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        '''Se utiliza query.add para añadir el resultado de búsqueda al query de name'''
        query.add(Q(fecha_estreno__contains=search_param), Q.OR)

        '''Guarda el resultado en el dict'''
        comedias = Comedia.objects.filter(query)
        context_dict = {
            'comedias': comedias
        }
    
    '''Renderiza el resultado de búsqueda en home.html, que es donde se ubica la página de búsqueda'''
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html",
    )    


@login_required
def comedia_actualiza(request, pk: int):
    comedia = Comedia.objects.get(pk=pk)

    if request.method == 'POST':
        comedia_form = ComediaForm(request.POST)
        if comedia_form.is_valid():
            data = comedia_form.cleaned_data
            comedia.name = data['name']
            comedia.fecha_estreno = data['fecha_estreno']
            comedia.duracion = data['duracion']
            comedia.sinopsis = data['sinopsis']
            comedia.save()

            comedias = Comedia.objects.all()
            context_dict = {
                'comedias': comedias
            }
            return render(
                request=request,
                context=context_dict,
                template_name="comedia/comedia_lista.html"
            )

    comedia_form = ComediaForm(model_to_dict(comedia))
    context_dict = {
        'comedia': comedia,
        'comedia_form': comedia_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='comedia/comedia_django_forms.html'
    )


@login_required
def borrar_comedia(request, pk: int):
    comedia = Comedia.objects.get(pk=pk)
    if request.method == 'POST':
        comedia.delete()

        comedias = Comedia.objects.all()
        context_dict = {
            'comedias': comedias
        }
        return render(
            request=request,
            context=context_dict,
            template_name="comedia/comedia_lista.html"
        )

    context_dict = {
        'comedia': comedias,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='comedia/comedia_conf_borrado.html'
    )    