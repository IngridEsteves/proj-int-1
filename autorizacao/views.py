from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def autorizacao(request):
    if request.method == "GET":
        return render(request, 'autorizacao.html')
    elif request.method == "POST":
        categoria = request.POST.get('categoria')
        tipo = request.POST.get('tipo')
        numero = request.POST.get('numero')
