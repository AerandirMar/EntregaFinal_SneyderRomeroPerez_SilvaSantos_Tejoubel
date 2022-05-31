from django.shortcuts import render
from django.db.models import Q
from bd_peliss.models import Accion, Terror, Comedia, CienciaFiccion
from bd_peliss.forms import AccionForm, TerrorForm, ComediaForm, CienciaFiccionForm


def index(request):
    return render(request, "bd_peliss/home.html")


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
        template_name="bd_peliss/accions.html"
    )


def terrors(request):
    '''Creamos la función en views para llamar a Terror (desde models) como un objeto y acumule todo en la variable terrors.
    Luego se guarda todo como key & value dentro del diccionario
    '''
    terrors = Terror.objects.all()

    context_dict = {
        'terrors': terrors
    }
    '''Renderizamos para visualizarlo en la url del template_name'''
    return render(
        request=request,
        context=context_dict,
        template_name="bd_peliss/terrors.html"
    )


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
        template_name="bd_peliss/comedias.html"
    )


def cienciaFiccions(request):
    '''Creamos la función en views para llamar a CienciaFiccion (desde models) como un objeto y acumule todo en la variable comedias.
    Luego se guarda todo como key & value dentro del diccionario
    '''
    cienciaFiccions = CienciaFiccion.objects.all()

    context_dict = {
            'cienciaFiccions': cienciaFiccions
    }
    '''Renderizamos para visualizarlo en la url del template_name'''
    return render(
        request=request,
        context=context_dict,
        template_name="bd_peliss/cienciaFiccions.html"
    )


def form_hmtl(request):
    '''Mediante el método Post llamamos a Models para visualizar la lista de películas ingresadas'''
    if request.method == 'POST':
        accion = Accion(name=request.POST['name'], fecha_estreno=request.POST['fecha_estreno'],
        duracion=request.POST['duracion'], sinopsis=request.POST['sinopsis'])

        '''Guardamos el listado consultado a la base de datos'''
        accion.save()

        '''Acá pedimos que lo consultado mediante Post y guardado mediante Save lo añada al diccionario'''
        accions = Accion.objects.all()
        context_dict = {
            'accions': accions
        }
        '''Visualiza en Template las películas añadidas al dict'''
        return render(
            request=request,
            context=context_dict,
            template_name="bd_peliss/accions.html"
        )

    return render(
        request=request,
        template_name='bd_peliss/formHTML.html'
    )


def accion_forms_django(request):
    '''Los comentarios aplican a las siguientes funciones
    terror_forms_django
    comedia_forms_django
    cienciaFiccion_forms_django
    '''
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

            '''Guarda los datos recolectados'''
            accion.save()

            '''Los acumula en el dict para renderizarlos posteriormente'''
            accions = Accion.objects.all()
            context_dict = {
                'accions': accions
            }
            return render(
                request=request,
                context=context_dict,
                template_name="bd_peliss/accions.html"
            )

    accion_form = AccionForm(request.POST)
    context_dict = {
        'accion_form': accion_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='bd_peliss/accion_django_forms.html'
    )


def terror_forms_django(request):
    if request.method == 'POST':
        terror_form = TerrorForm(request.POST)
        if terror_form.is_valid():
            data = terror_form.cleaned_data
            terror = Terror(
                name=data['name'],
                fecha_estreno=data['fecha_estreno'],
                duracion=data['duracion'],
                sinopsis=data['sinopsis'],
            )
            terror.save()

            terrors = Terror.objects.all()
            context_dict = {
                'terrors': terrors
            }
            return render(
                request=request,
                context=context_dict,
                template_name="bd_peliss/terrors.html"
            )

    terror_form = TerrorForm(request.POST)
    context_dict = {
        'terror_form': terror_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='bd_peliss/terror_django_forms.html'
    )


def cienciaFiccion_forms_django(request):
    if request.method == 'POST':
        cienciaFiccion_form = CienciaFiccionForm(request.POST)
        if cienciaFiccion_form.is_valid():
            data = cienciaFiccion_form.cleaned_data
            cienciaFiccion = CienciaFiccion(
                name=data['name'],
                fecha_estreno=data['fecha_estreno'],
                duracion=data['duracion'],
                sinopsis=data['sinopsis'],
            )
            cienciaFiccion.save()

            cienciaFiccions = CienciaFiccion.objects.all()
            context_dict = {
                    'cienciaFiccions': cienciaFiccions
            }
            return render(
                request=request,
                context=context_dict,
                template_name="bd_peliss/cienciaFiccions.html"
            )

    cienciaFiccion_form = CienciaFiccionForm(request.POST)
    context_dict = {
        'cienciaFiccion_form': cienciaFiccion_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='bd_peliss/cienciaFiccion_django_forms.html'
    )


def comedia_forms_django(request):
    if request.method == 'POST':
        comedia_form = ComediaForm(request.POST)
        if comedia_form.is_valid():
            data = comedia_form.cleaned_data
            comedia = Comedia(
                name=data['name'],
                fecha_estreno=data['fecha_estreno'],
                duracion=data['duracion'],
                sinopsis=data['sinopsis'],
            )
            comedia.save()

            comedias = Comedia.objects.all()
            context_dict = {
                'comedias': comedias
            }
            return render(
                request=request,
                context=context_dict,
                template_name="bd_peliss/comedias.html"
            )

    comedia_form = ComediaForm(request.POST)
    context_dict = {
        'comedia_form': comedia_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='bd_peliss/comedia_django_forms.html'
    )


def search(request):
    '''Los comentarios de esta función también son válidos para:
    searchTer
    searchCom
    searchSci
    '''

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
        template_name="bd_peliss/home.html",
    )


def searchTer(request):
    '''Si no se ingresa ningún valor en los campos, no arroja ningún mensaje'''
    context_dict = dict() 
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        terrors = Terror.objects.filter(name__contains=search_param)
        context_dict = {
            'terrors': terrors
        }
    elif request.GET['fecha_estreno_search']:
        search_param = request.GET['fecha_estreno_search']
        terrors = Terror.objects.filter(fecha_estreno__contains=search_param)
        context_dict = {
            'terrors': terrors
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(fecha_estreno__contains=search_param), Q.OR)
        terrors = Terror.objects.filter(query)
        context_dict = {
            'terrors': terrors
        }

    return render(
        request=request,
        context=context_dict,
        template_name="bd_peliss/home.html",
    )


def searchCom(request):
    '''Si no se ingresa ningún valor en los campos, no arroja ningún mensaje'''
    context_dict = dict() 
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
        query.add(Q(fecha_estreno__contains=search_param), Q.OR)
        comedias = Comedia.objects.filter(query)
        context_dict = {
            'comedias': comedias
        }

    return render(
        request=request,
        context=context_dict,
        template_name="bd_peliss/home.html",
    )


def searchSci(request):
    '''Si no se ingresa ningún valor en los campos, no arroja ningún mensaje'''
    context_dict = dict() 
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        cienciaFiccions = CienciaFiccion.objects.filter(name__contains=search_param)
        context_dict = {
            'cienciaFiccions': cienciaFiccions
        }
    elif request.GET['fecha_estreno_search']:
        search_param = request.GET['fecha_estreno_search']
        cienciaFiccions = CienciaFiccion.objects.filter(fecha_estreno__contains=search_param)
        context_dict = {
            'cienciaFiccions': cienciaFiccions
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(fecha_estreno__contains=search_param), Q.OR)
        cienciaFiccions = CienciaFiccion.objects.filter(query)
        context_dict = {
            'cienciaFiccions': cienciaFiccions
        }

    return render(
        request=request,
        context=context_dict,
        template_name="bd_peliss/home.html",
    )


def nosotros(request):
    return render(request, "bd_peliss/nosotros.html")


def contacto(request):
    return render(request, "bd_peliss/contacto.html")
