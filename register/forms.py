from django.forms import ModelForm
from .models import ObjectiveKeyResult
from django.utils.translation import gettext_lazy as _

class OkrForm(ModelForm):
    class Meta:
        model = ObjectiveKeyResult
        fields = ['integrante','objetivo','resultado_1','resultado_2','resultado_3','resultado_4','resultado_5',]