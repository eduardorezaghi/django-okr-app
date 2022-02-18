import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Integrante, ObjectiveKeyResult

from .forms import OkrForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = OkrForm(request.POST)
        if form.is_valid():
            form.save()
            intg = form.cleaned_data.get('integrante')
            messages.success(request, f"OKR criada para o integrante {intg}")
            return HttpResponseRedirect('/register/')
    else:
        form = OkrForm()

    return render(request, 'register/form.html', {'form': form})
