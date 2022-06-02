from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Dog, Group
from django.urls import reverse

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

class DogList(TemplateView):
    template_name = "dog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        breed = self.request.GET.get("breed")
        if breed != None:
            context["dogs"] = Dog.objects.filter(name__icontains=breed)
            context["dogs"] = f"Searching for {breed}"
        else:
            context["dogs"] = Dog.objects.all()

            context["header"] = "Dog Breeds"
        return context

class DogCreate(CreateView):
    model = Dog
    fields = ['breed', 'img', 'about']
    template_name = "dog_create.html"
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})

class DogDetail(DetailView):
    model = Dog
    template_name = "dog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'img', 'about']
    template_name = "dog_update.html"
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})

class DogDelete(DeleteView):
    model = Dog
    template_name = 'dog_delete.html'
    success_url = '/dogs/'

class GroupDogAssoc(View):

    def get(self, request, pk, dog_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Group.objects.get(pk=pk).dogs.remove(dog_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Group.objects.get(pk=pk).dogs.add(dog_pk)
        return redirect('home')
