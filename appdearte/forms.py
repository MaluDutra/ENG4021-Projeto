from django.forms import ModelForm
from appdearte.models import Events

class AvaliationForm(ModelForm):
    class Meta:
        model = Events
        fields = ["recomendation"]

form = AvaliationForm()