from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .form import UserCreationForm, MyUserCreationForm


class RegisterView(CreateView):
    form_class = MyUserCreationForm

    template_name = 'account/register.html'


