from django.shortcuts import render



# Create your views here.
def home(request):
    resposta = 'resposta do blog vinda do app blog'
    return render(
        request, 
        'blog/index.html'
    )

def exemplo(request):
    return render(
        request,
        'blog/exemplo.html'
    )