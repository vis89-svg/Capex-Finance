# events/urls.py
from django.urls import path
from .views import main_view, event_creation_view, login_view, add_finance_view

urlpatterns = [
    path('index/', main_view, name='index'),
    path('create-event/', event_creation_view, name='create_event'),
    path('add-finance/<int:event_id>/', add_finance_view, name='add_finance'),  # New path for adding finance
    path('', login_view, name='login'),
]
