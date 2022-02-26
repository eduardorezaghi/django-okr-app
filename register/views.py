"""
Views implementing Model and Serializer logic for our API.
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view

from .forms import OkrForm
from .models import Integrante, ObjectiveKeyResult
from .serializers import IntegranteSerializer, ObjectiveKeyResultSerializer

@api_view(['GET', 'POST'])
def index(request):
    """
    Index view-function dealing with template rendering
    """
    if request.method == 'POST':
        form = OkrForm(request.POST)
        if form.is_valid():
            form.save()
            intg = form.cleaned_data.get('integrante')
            messages.success(request, f"OKR criada para o integrante {intg}")
            return HttpResponseRedirect('/register/')
        messages.error(request, "Dados inseridos são inválidos. Corrija-os e insira novamente!")
    else:
        form = OkrForm()

    return render(request, 'register/form.html', {'form': form})

class OkrViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for a Okr resource.
    """
    queryset = ObjectiveKeyResult.objects.all().order_by('integrante')
    serializer_class = ObjectiveKeyResultSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class IntegranteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for a Integrante resource.
    """
    queryset = Integrante.objects.all()
    serializer_class = IntegranteSerializer
