from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Contact, Services
from apps.main.form import ContactForm
from apps.blog.models import BlogPost
from apps.services.models import ServicesPost
from apps.rooms.models import Room


class HomePageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self,  **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt['services'] = Services.objects.all()
        cnt['blog_list'] = BlogPost.objects.order_by('-id')[:3]
        cnt['Services_all'] = ServicesPost.objects.order_by('-id')[:5]
        # check_in = request.GET.get('checkin-date')
        # check_out = request.GET.get('checkout-date')
        # max_adults = request.GET.get('adults')
        # max_children = request.GET.get('children')
        # price = request.GET.get('price')
        # rooms = Room.objects.all()
        # if check_in and check_out:
        #     rooms = rooms.filter(~Q(rooms_booking__check_in__lte=check_out) | ~Q(rooms_booking__check_out__gte=check_in))
        #     if int(max_adults) != 0 or int(max_children) != 0:
        #         rooms_max_person = rooms.filter(Q(max_person=int(max_adults) + int(max_children)))
        #         rooms = rooms.intersection(rooms_max_person)
        return cnt


class ContactView(CreateView):
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy('main:contact')


class AboutView(TemplateView):
    def get_context_data(self, **kwargs):
        cnt = super(AboutView, self).get_context_data(**kwargs)
        cnt['room_3'] = Room.objects.order_by('-id')[:3]
        return cnt
    template_name = 'main/about.html'


