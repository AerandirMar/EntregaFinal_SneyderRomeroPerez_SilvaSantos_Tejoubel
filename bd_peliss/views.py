from django.shortcuts import render
from django.db.models import Q
from bd_peliss.models import Accion, Terror, Comedia, CienciaFiccion
from bd_peliss.forms import AccionForm, TerrorForm, ComediaForm, CienciaFiccionForm


def index(request):
    return render(request, "bd_peliss/home.html")


def accions(request):
    accions = Accion.objects.all()

    context_dict = {
        'accions': accions
    }

    return render(
        request=request,
        context=context_dict,
        template_name="bd_peliss/accions.html"
    )


def terrors(request):
    terrors = Terror.objects.all()

    context_dict = {
        'terrors': terrors
    }

    return render(
        request=request,
        context=context_dict,
        template_name="bd_peliss/terrors.html"
    )


def comedias(request):
    comedias = Comedia.objects.all()

    context_dict = {
        'comedias': comedias
    }

    return render(
        request=request,
        context=context_dict,
        template_name="bd_peliss/comedias.html"
    )


def cienciaFiccions(request):
    cienciaFiccions = CienciaFiccion.objects.all()

    context_dict = {
            'cienciaFiccions': cienciaFiccions
    }

    return render(
        request=request,
        context=context_dict,
        template_name="bd_peliss/cienciaFiccions.html"
    )


def form_hmtl(request):

    if request.method == 'POST':
        accion = Accion(name=request.POST['name'], fecha_estreno=request.POST['fecha_estreno'],
        duracion=request.POST['duracion'], sinopsis=request.POST['sinopsis'])
        accion.save()

        accions = Accion.objects.all()
        context_dict = {
            'accions': accions
        }

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
    if request.method == 'POST':
        accion_form = AccionForm(request.POST)
        if accion_form.is_valid():
            data = accion_form.cleaned_data
            accion = Accion( 
                name=data['name'],
                fecha_estreno=data['fecha_estreno'],
                duracion=data['duracion'],
                sinopsis=data['sinopsis'],                       
            )
            accion.save()

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
                template_name="bd_peliss/terror_django_forms.html"
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
                template_name="bd_peliss cienciaFiccions.html"
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
    '''Si no se ingresa ningún valor en los campos, no arroja ningún mensaje'''
    context_dict = dict() 
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
        query.add(Q(fecha_estreno__contains=search_param), Q.OR)
        accions = Accion.objects.filter(query)
        context_dict = {
            'accions': accions
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
