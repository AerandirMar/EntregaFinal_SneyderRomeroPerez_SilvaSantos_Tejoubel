import os
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render

from user.forms import UserRegisterForm, UserEditForm, AvatarForm
from user.models import Avatar


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'home/main.html', {'mensaje': 'Usuario creado'})

            #messages.success(request, "Usuario creado exitosamente!")
            #return redirect("user:user-login")
    else:        
        form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form},
        template_name="user/register.html",
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "home/main.html", {"mensaje":f"Bienvenido {user}"} )

            else:
                return render(request, "home/main.html", {"mensaje":"Error, datos incorrectos"})    

        return render(
            request=request,
            context={'form': form},
            template_name="user/login.html",
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="user/login.html",
    )


def logout_request(request):
      logout(request)
      return redirect("user:user-login")


@login_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user.email = info['email']
            user.password1 = info['password1']
            user.pasword2 = info['password2']
            user.save()

            return render(request, "home/main.html")
            #return redirect('home:main')

    else: 
        form = UserEditForm(initial={'email':user.email})

    return render(request, 'user/user_form.html', {'form':form, 'user':user})
    #form= UserEditForm(model_to_dict(user))
    #return render(
    #    request=request,
    #    context={'form': form},
    #    template_name="user/user_form.html",
    #)


@login_required
def avatar_load(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('home:main')

    form= AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="user/avatar_form.html",
    )
