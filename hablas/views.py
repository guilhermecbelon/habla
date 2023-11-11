from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from datetime import datetime

class ListHablasView(generic.ListView):
    model = Habla
    template_name = 'hablas/index.html'
    context_object_name = 'habla_list'

    def get_queryset(self):
        return reversed(Habla.objects.all())

class DetailHablaView(generic.DetailView):
    model = Habla
    template_name = 'hablas/detail.html'
    context_object_name = 'habla'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_data = Comment.objects.filter(habla=self.object)
        context['comment_list'] = reversed(comment_data)
        return context

class CreateHablaView(generic.CreateView):
    model = Habla
    form_class = HablaForm
    template_name = 'hablas/create.html'
    success_url = reverse_lazy('hablas:index') 

    def form_valid(self, form):
        form.instance.post_date = datetime.now()
        return super().form_valid(form)

def delete_habla(request,habla_id):
    habla = Habla.objects.get(id=habla_id)
    habla.delete()    
    return redirect('hablas:index')

def edit_habla(request,habla_id):
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
    
class EditHablaView(generic.UpdateView):
    model = Habla
    form_class = HablaForm
    template_name = 'hablas/edit.html'

    def form_valid(self, form):
        habla = form.save(commit=False)
        habla.post_date = datetime.now()
        habla.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('hablas:detail', kwargs={'pk': self.object.pk})
    
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


