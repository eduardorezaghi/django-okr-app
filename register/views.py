from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import OkrForm
from .models import Integrante, ObjectiveKeyResult
from .permissions import IsOwnerOrReadOnly
from .serializers import IntegranteSerializer, ObjectiveKeyResultSerializer, UserSerializer

from rest_framework import viewsets
from rest_framework import permissions

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
    else:
        form = OkrForm()

    return render(request, 'register/form.html', {'form': form})

class OkrViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = ObjectiveKeyResult.objects.all()
    serializer_class = ObjectiveKeyResultSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class IntegranteViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Integrante.objects.all()
    serializer_class = IntegranteSerializer
