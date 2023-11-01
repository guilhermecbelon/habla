from django.http import HttpResponseRedirect
from django.urls import reverse
from .temp_data import habla_data
from django.shortcuts import render


def detail_habla(request, habla_id):
    context = {'habla': habla_data[habla_id - 1]}
    return render(request, 'hablas/detail.html', context)


def list_hablas(request):
    context = {"habla_list": habla_data}
    return render(request, 'hablas/index.html', context)


def search_hablas(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "habla_list": [
                m for m in habla_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'hablas/search.html', context)


def create_habla(request):
    if request.method == 'POST':
        habla_data.append({
            'name': request.POST['name'],
            'release_year': request.POST['release_year'],
            'poster_url': request.POST['poster_url']
        })
        return HttpResponseRedirect(
            reverse('hablas:detail', args=(len(habla_data), )))
    else:
        return render(request, 'hablas/create.html', {})