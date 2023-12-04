from django.forms import ModelForm
from appdearte.models import Events

class AvaliationForm(ModelForm):
    class Meta:
        model = Events
        fields = ["recomendation"]

form = AvaliationForm()

class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = ["name", "link", "price", "date", "time", "category", "location"]

form_event = EventsForm()