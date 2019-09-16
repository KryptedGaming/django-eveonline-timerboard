from django.forms import ModelForm
from .models import EveTimer 

class EveTimerForm(ModelForm):
    class Meta:
        model = EveTimer 
        fields = ['name', 'type', 'timer', 'groups']