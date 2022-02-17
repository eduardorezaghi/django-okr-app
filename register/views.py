import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Integrante, ObjectiveKeyResult

from .forms import OkrForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = OkrForm(request.POST)
        if form.is_valid():
            okr = ObjectiveKeyResult()
            okr.integrante = form.cleaned_data['integrante']
            okr.objetivo = form.cleaned_data['objetivo']
            okr.resultado_1 = form.cleaned_data['resultado_1']
            okr.resultado_2 = form.cleaned_data['resultado_2']
            okr.resultado_3 = form.cleaned_data['resultado_3']
            okr.resultado_4 = form.cleaned_data['resultado_4']
            okr.resultado_5 = form.cleaned_data['resultado_5']
            
            print(form.cleaned_data['integrante'])
            print(form.cleaned_data['objetivo'])
            print(form.cleaned_data['resultado_1'])
            print(form.cleaned_data['resultado_2'])
            print(form.cleaned_data['resultado_3'])
            print(form.cleaned_data['resultado_4'])
            print(form.cleaned_data['resultado_5'])
            form.save()
            return HttpResponseRedirect('/register/')
    else:
        form = OkrForm()

    return render(request, 'register/form.html', {'form': form})
