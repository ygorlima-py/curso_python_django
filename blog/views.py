from django.shortcuts import render



# Create your views here.
def home(request):
    resposta = 'resposta do blog vinda do app blog'
    return render(
        request, 
        'blog/index.html',
        context=dict(
            text='Aqui é o blog e ' \
            'estou usando adição de texto por contexto',
            title='Blog'
        )
    )

def exemplo(request):
    return render(
        request,
        'blog/exemplo.html',
        context=dict(
            text='Exemplo da pagina Blog',
            title='Exemplo'
        )
    )