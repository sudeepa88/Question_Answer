from django import forms 
from .models import *

class uform(forms.ModelForm):
    class Meta:
        model=User
        fields="_all_"