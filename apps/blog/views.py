from urllib import request

from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Tag, Content
from django.views.generic import TemplateView, CreateView, ListView


class BlogListView(ListView):
    queryset = BlogPost.objects.all()
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['object_3'] = BlogPost.objects.order_by('-id')[:3]
        ctx['tags'] = Tag.objects.all()
        return ctx


def blogdetail(request, slug):
    blogs = BlogPost.objects.order_by('-id')[:3]
    blog = get_object_or_404(BlogPost, slug=slug)
    tags = Tag.objects.all()
    context = {
        'blog': blog,
        'blogs': blogs,
        'tags': tags,

    }
    return render(request, 'blog/single-blog.html', context)
