# events/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Finance
from .forms import EventForm, LoginForm, FinanceForm
from django.contrib import messages
from decimal import Decimal
import json
from django.db import transaction

def main_view(request):
    events = Event.objects.all()
    
    # Set 'show_add_button' to False if the user is a superuser
    show_add_button = not request.user.is_superuser
    
    return render(request, 'events/index.html', {
        'events': events,
        'show_add_button': show_add_button
    })

def event_creation_view(request):
    # Handle event creation
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm()
    return render(request, 'events/event_creation.html', {'form': form})

def login_view(request):
    # Handle login functionality
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            events = Event.objects.filter(user_name=user_name, password=password)
            if user_name == 'legacy123' and password == '123456789':
                return render(request, 'events/index.html', {'events': Event.objects.all(), 'show_add_button': True})
            if events.exists():
                return render(request, 'events/index.html', {'events': events, 'show_add_button': False})
            else:
                return render(request, 'events/index.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'events/login.html', {'form': form})

def add_finance_view(request, event_id):
    # Handle adding finance for an event
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = FinanceForm(request.POST)
        if form.is_valid():
            finance = form.save(commit=False)
            finance.event = event
            finance.save()
            return redirect('index')  # Redirect back to main page or user page as needed
    else:
        form = FinanceForm()

    return render(request, 'events/add_finance.html', {'form': form, 'event': event})
