from django.shortcuts import render
import requests 
import json



# Create your views here.

# Página Home
def home(request):
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts_json = posts.json()

    context = dict(
        # text='Meu Blog',
        posts=posts_json,
    )

    return render(
        request, 
        'blog/index.html',
        context=context,
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


if __name__ == "__main__":
    result = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(result.json())