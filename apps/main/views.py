from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Contact
from apps.main.form import ContactForm


class HomePageView(TemplateView):
    template_name = 'main/index.html'


class ContactView(CreateView):
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy('main:contact')
