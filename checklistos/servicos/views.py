from django.shortcuts import render

# Create your views here.
from checklistos.servicos.models import Servico


def index(request):
    query_set = Servico.objects.order_by('nomelongo')
    ctx = {
        'servicos': list(query_set)
    }

    return render(request, 'servicos/index.html', context=ctx)
