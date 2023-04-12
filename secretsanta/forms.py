from django import forms
from .models import SantaGroup


class SantaGroupForm(forms.ModelForm):

    class Meta:
        model = SantaGroup
        fields = ('name', 'description', 'distribution_date',)
