from django import forms
from .models import Uang_keluar, Uang_masuk
from django.contrib.auth.models import User
from django.utils import timezone

class UangMutationForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    user_id = forms.ModelChoiceField(label="User",required=True,queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'select select-bordered w-full max-w-xs'}))
    datetime = forms.DateTimeField(label="Tanggal",initial=timezone.now, required=True, widget=forms.DateTimeInput(attrs={'placeholder': 'Tanggal', 'type': 'datetime-local', 'class': 'input input-bordered w-full max-w-xs', 'step':"1"}))
    nominal = forms.IntegerField(label="Nominal",min_value=0, required=True,widget=forms.NumberInput(attrs={'placeholder': 'Nominal', 'class': 'input input-bordered w-full max-w-xs'}))