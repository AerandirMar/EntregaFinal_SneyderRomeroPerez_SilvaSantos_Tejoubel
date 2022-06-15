from django.shortcuts import render
from django.db.models import Q
from terror.models import Terror
from terror.forms import TerrorForm
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict


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
        template_name="terror/terror_lista.html"
    )


@login_required
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
                template_name="terror/terror_lista.html"
            )

    terror_form = TerrorForm(request.POST)
    context_dict = {
        'terror_form': terror_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='terror/terror_django_forms.html'
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
        template_name="terror/home.html",
    )


@login_required
def terror_actualiza(request, pk: int):
    terror = Terror.objects.get(pk=pk)

    if request.method == 'POST':
        terror_form = TerrorForm(request.POST)
        if terror_form.is_valid():
            data = terror_form.cleaned_data
            terror.name = data['name']
            terror.fecha_estreno = data['fecha_estreno']
            terror.duracion = data['duracion']
            terror.sinopsis = data['sinopsis']
            terror.save()

            terrors = Terror.objects.all()
            context_dict = {
                'terrors': terrors
            }
            return render(
                request=request,
                context=context_dict,
                template_name="terror/terror_lista.html"
            )

    terror_form = TerrorForm(model_to_dict(terror))
    context_dict = {
        'terror': terror,
        'terror_form': terror_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='terror/terror_django_forms.html'
    )


@login_required
def borrar_terror(request, pk: int):
    terror = Terror.objects.get(pk=pk)
    if request.method == 'POST':
        terror.delete()

        terrors = Terror.objects.all()
        context_dict = {
            'terrors': terrors
        }
        return render(
            request=request,
            context=context_dict,
            template_name="terror/terror_lista.html"
        )

    context_dict = {
        'terror': terrors,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='terror/terror_conf_borrado.html'
    )    