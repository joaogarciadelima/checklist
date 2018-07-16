from django.shortcuts import render

# Create your views here.
from checklistos.produtos.models import Produto


def index(request):
    query_set = Produto.objects.order_by('nomelongo')
    ctx = {
        'produtos': list(query_set)
    }

    return render(request, 'produtos/index.html', context=ctx)
