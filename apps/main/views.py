from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Contact, Services
from apps.main.form import ContactForm
from apps.blog.models import BlogPost
from apps.services.models import ServicesPost


class HomePageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt['services'] = Services.objects.all()
        cnt['blog_list'] = BlogPost.objects.order_by('-id')[:3]
        cnt['Services_all'] = ServicesPost.objects.order_by('-id')[:5]
        return cnt


class ContactView(CreateView):
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy('main:contact')


