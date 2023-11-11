from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime

class ListHablasView(generic.ListView):
    model = Habla
    template_name = 'hablas/index.html'
    context_object_name = 'habla_list'

    def get_queryset(self):
        return reversed(Habla.objects.all())
    
def detail_habla(request, habla_id):
    habla_data = get_object_or_404(Habla,pk=habla_id)
    comment_data = Comment.objects.filter(habla_id=habla_id)
    context = {'habla': habla_data, 'comment_list':reversed(comment_data)}
    return render(request, 'hablas/detail.html', context)



class DetailHablaView(generic.DetailView):
    model = Habla
    template_name = 'hablas/detail.html'
    context_object_name = 'habla'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_data = Comment.objects.filter(habla=self.object)
        context['comment_list'] = reversed(comment_data)
        return context

def create_habla(request):
    if request.method == 'POST':
        form = HablaForm(request.POST)
        if form.is_valid():
            habla_text = request.POST['text']
            author_id = request.POST['author']
            habla_author = User.objects.get(id=author_id)
            cattegory = request.POST['cattegory']
            habla = Habla(text=habla_text,
                          post_date = datetime.now(),
                        author = habla_author,
                        cattegory = cattegory)
            habla.save()
            return HttpResponseRedirect(
                reverse('hablas:detail', args=(habla.id, )))
    else:
        form = HablaForm()
        context = {'form': form}
        return render(request, 'hablas/create.html', context)
    
def delete_habla(request,habla_id):
    habla = Habla.objects.get(id=habla_id)
    habla.delete()    
    return redirect('hablas:index')

def edit_habla(request,habla_id):
    print(request)
    if request.method == 'POST':
        form = HablaForm(request.POST)
        if form.is_valid():
            habla = Habla.objects.get(id=habla_id)
            habla.text = request.POST['text']
            author_id = request.POST['author']            
            habla.cattegory = request.POST['cattegory']
            habla.author = User.objects.get(id=author_id)
            habla.post_date = datetime.now()
            habla.save()
            return HttpResponseRedirect(
                reverse('hablas:detail', args=(habla.id, )))
    else:
        form = HablaForm()
        context = {'form': form}
        return render(request, 'hablas/edit.html', context)
    
def like_habla(request,habla_id):    
    habla = Habla.objects.get(id=habla_id)
    habla.likes+=1
    habla.save()
    return redirect('hablas:index')
    
    
def create_comment(request, habla_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_text = request.POST['comment_text']
            author_id = request.POST['author']
            comment_author = User.objects.get(id=author_id)
            habla = Habla.objects.get(id=habla_id) 
            comment = Comment(comment_text=comment_text,
                          post_date = datetime.now(),
                          habla = habla,
                        author = comment_author )
            comment.save()
            return HttpResponseRedirect(
                reverse('hablas:detail', args=(habla.id, )))
    else:
        form = CommentForm()
        context = {'form': form}
        return render(request, 'hablas/create_comment.html', context)
    


def search_hablas(request):
    context={}
    if request.GET.get("query", False):
        search_term = request.GET["query"].lower()
        context = {'search_term':search_term}
        habla_list = Habla.objects.filter(cattegory__icontains=search_term)
        if len(habla_list)> 0:
            context["habla_list"]= (habla_list)
    return render(request, "hablas/search.html", context)

def search_hablas_by_tag(request, habla_cattegory):
    context = {'search_term':habla_cattegory}
    habla_list = Habla.objects.filter(cattegory__icontains=habla_cattegory)
    if len(habla_list)> 0:
        context["habla_list"]= (habla_list)
    return render(request, "hablas/search.html", context)


