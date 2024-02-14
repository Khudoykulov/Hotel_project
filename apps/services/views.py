from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView
from .models import ServicesPost, Category


class ServicesListView(TemplateView):
    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt['services_list'] = ServicesPost.objects.order_by('-id')
        cnt['services_3'] = ServicesPost.objects.order_by('-id')[:3]
        cnt['categories'] = Category.objects.all()
        return cnt

    template_name = 'services/service_list.html'


def service_detail(request, slug):
    service_3 = ServicesPost.objects.order_by('-id')[:3]
    blog = get_object_or_404(ServicesPost, slug=slug)
    categories = Category.objects.all()
    context = {
        'blog': blog,
        'service_3': service_3,
        'categories': categories,

    }
    return render(request, 'services/service_detail.html', context)
