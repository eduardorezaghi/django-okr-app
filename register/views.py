from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages


from .forms import OkrForm
from .permissions import IsOwnerOrReadOnly
from .serializers import IntegranteSerializer, ObjectiveKeyResultSerializer, UserSerializer
from .models import Integrante, ObjectiveKeyResult

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view

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

class OkrViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = ObjectiveKeyResult.objects.all()
    serializer_class = ObjectiveKeyResultSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
