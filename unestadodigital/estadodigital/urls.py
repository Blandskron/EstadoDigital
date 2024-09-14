from django.urls import path
from .views import contact_view, confirmation_view

urlpatterns = [
    path('', contact_view, name='home'),
    path('confirmation/', confirmation_view, name='confirmation'),
]