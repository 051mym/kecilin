from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ("username", "email",)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
            'email': forms.EmailInput(attrs={'class': 'input input-bordered w-full max-w-xs'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
