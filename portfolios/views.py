from django.shortcuts import render
from .models import DadosPessoais


def portfolio_exibir(request):
    pessoa = DadosPessoais.objects.all()
    # pessoa = DadosPessoais.objects.filter()
    context = {'pessoa': pessoa}
    return render(request, 'portfolios/portfolio_exibir.html', context)
