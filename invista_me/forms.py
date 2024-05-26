from django.forms import ModelForm
from .models import investimento

class InvestimentoForm(ModelForm):
    class Meta:
        model = investimento
        fields ='__all__'
