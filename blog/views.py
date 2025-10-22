from django.shortcuts import render
import requests 
from django.http import HttpRequest, Http404



# Create your views here.

# Página Home
def blog(request: HttpRequest):
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
def exemplo(request: HttpRequest):

    print (request)

    context = dict(
        text='Exemplo da página Blog',
        title='Exemplo',
    )

    return render(
        request,
        'blog/exemplo.html',
        context,
    )

def post(request: HttpRequest, post_id: int):

    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts_json = posts.json()

    found_post = None

    for post in posts_json:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post Não existe')
        # Aqui adicionamo uma excessão, erro 404, significa quando o servidor não encontrou a pagina solicitada
        # Outro ponto, sem essa excessão ele lança erro 500, que não é vdd, pois o erro é do cliente
    
    context = dict(
        # text='Meu Blog',
        post=found_post,
        title=found_post['title'],
    )

    return render(
        request, 
        'blog/post.html',
        context=context,
    )


if __name__ == "__main__":
    result = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(result.json())

