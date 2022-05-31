# Instrucciones detalladas de la página

- Búsqueda de películas por género desde la pestaña Home
```bash
http://127.0.0.1:8000/bd-peliss/
```

- El buscador de películas (según género) buscará por "Nombre", "Año" (fecha de estreno), y búsqueda general (referente a los primeros dos campos)

- En las siguientes URLs se podrán listar las películas del genero que precises ver.
```bash
http://127.0.0.1:8000/bd-peliss/accions
http://127.0.0.1:8000/bd-peliss/terrors
http://127.0.0.1:8000/bd-peliss/comedias
http://127.0.0.1:8000/bd-peliss/sci-fi
```

- También se podrá añadir alguna otra película de tu interés, linkeando a "Ingresar nueva película" donde se te redirigirá al link detallado a continuación (el link varía con el género de la película).
```bash
http://127.0.0.1:8000/bd-peliss/accion-django-forms
http://127.0.0.1:8000/bd-peliss/terror-django-forms
http://127.0.0.1:8000/bd-peliss/comedia-django-forms
http://127.0.0.1:8000/bd-peliss/scifi-django-forms
```

- Deberás completar los campos
```bash
- Nombre
- Fecha de estreno (en formato AAAA-MM-DD)
- Duración (solo aceptará números)
- Sinopsis (Un breve comentario de qué trata la película)
```