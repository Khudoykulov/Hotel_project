from urllib import request

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Tag, Comments
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from .form import CommentForm


class BlogListView(View):
    template_name = 'blog/blog.html'

    def get(self, request, *args, **kwargs):
        posts = BlogPost.objects.all()
        tag = request.GET.get('tag')
        if tag:
            posts = BlogPost.objects.filter(tags__name__exact=tag)
        paginator = Paginator(posts, 3)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        object_3 = BlogPost.objects.order_by('-id')[:3]
        tags = Tag.objects.all()
        ctx = {
            'object_list': posts,
            'object_3': object_3,
            'tags': tags

        }
        return render(request, 'blog/blog.html', ctx)


def blogdetail(request, slug):
    blogs = BlogPost.objects.order_by('-id')[:3]
    blog = get_object_or_404(BlogPost, slug=slug)
    tags = Tag.objects.all()
    comments = Comments.objects.filter(blog=blog, parent__isnull=True).order_by('-id')
    form = CommentForm()
    cid = request.GET.get('cid')
    if request.method == 'POST':
        form = CommentForm(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)

            obj.blog = blog
            print(obj.author)
            print('///')
            print(request.user.id)
            obj.author_id = request.user.id
            if cid:
                obj.parent_id = cid
            form.save()
            messages.success(request, 'You have successfully commentary')
            return redirect(f'.#comment-{obj.id}')
    context = {
        'blog': blog,
        'blogs': blogs,
        'tags': tags,
        'form': form,
        'comments': comments

    }
    return render(request, 'blog/single-blog.html', context)


