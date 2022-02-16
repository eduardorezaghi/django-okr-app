from django.shortcuts import render
from django.views import generic
from .models import Integrante

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'register/form.html'
    context_object_name = "integrante_list"

    def get_queryset(self):
        return Integrante.objects.all()