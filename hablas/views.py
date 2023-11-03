from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from .forms import HablaForm
from django.shortcuts import render, get_object_or_404
from datetime import datetime

def detail_habla(request, habla_id):
    habla_data = get_object_or_404(Habla,pk=habla_id)
    context = {'habla': habla_data}
    return render(request, 'hablas/detail.html', context)

def list_hablas(request):
    habla_data = Habla.objects.all()
    context = {"habla_list": habla_data}
    return render(request, 'hablas/index.html', context)

def search_hablas(request):
    habla_data = Habla.objects.all()
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
        form = HablaForm(request.POST)
        if form.is_valid():
            habla_text = request.POST['text']
            author_id = request.POST['author']
            habla_author = User.objects.get(id=author_id)
            print(habla_author, habla_text)
            habla = Habla(text=habla_text,
                          post_date = datetime.now(),
                        author = habla_author)
            habla.save()
            return HttpResponseRedirect(
                reverse('hablas:detail', args=(habla.id, )))
    else:
        form = HablaForm()
        context = {'form': form}
        return render(request, 'hablas/create.html', context)