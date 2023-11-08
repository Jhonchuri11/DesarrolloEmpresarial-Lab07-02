from django.forms import ModelForm
from .models import *

class Matriculaform(ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'
    
