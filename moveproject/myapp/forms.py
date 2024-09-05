# events/forms.py
from django import forms
from .models import Event, Finance

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'user_name', 'password']

class LoginForm(forms.Form):
    user_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'style': 'box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25)'
            }),
        
        label=''
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'style': 'box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25)'
            }),
        label=''
    )

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ['from_person', 'to_person', 'description', 'amount', 'date_event', 'mode','amount']
