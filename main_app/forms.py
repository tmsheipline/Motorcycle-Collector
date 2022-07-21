from django.forms import ModelForm
from .models import Washing

class WashingForm(ModelForm):
  class Meta:
    model = Washing
    fields = ['date', 'time']