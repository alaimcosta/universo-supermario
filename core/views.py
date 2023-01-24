from django.shortcuts import render
from .models import GeneroJogo, Jogo

def index(request):
    context={}
    return render(request, 'index.html', context)


def salvar(request):
    nomeJogo = request.POST.get("task_name")
    person = request.POST.get("task_personagem")
    genero = request.POST.get("task_genero")
    ano = request.POST.get("task_ano")

    Jogo.objects.create(nomeJogo=nomeJogo)
    Jogo.objects.create(person=person)
    GeneroJogo.objects.create(genero=genero)
    Jogo.objects.create(ano=ano)
    return render(request, 'index.html')