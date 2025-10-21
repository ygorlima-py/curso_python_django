from django.shortcuts import render



# Create your views here.

# Página Home
def home(request):
    text = 'Aqui é o blog e estou usando adição de texto por contexto'
    title = 'Blog'
    context = dict(
        text=text,
        title=title,
    )

    return render(
        request, 
        'blog/index.html',
        context
    )

# Pagina Exemplo
def exemplo(request):

    context = dict(
        text='Exemplo da página Blog',
        title='Exemplo',
    )

    return render(
        request,
        'blog/exemplo.html',
        context,
    )