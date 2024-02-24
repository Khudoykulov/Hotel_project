from urllib import request

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Tag, Comments
from django.views.generic import TemplateView, CreateView, ListView
from .form import CommentForm


class BlogListView(ListView):
    queryset = BlogPost.objects.all()
    paginate_by = 3
    template_name = 'blog/blog.html'
    # def get(self, request, *args, **kwargs):
    #     ctx = self.get_context_data(**kwargs)
    #     ctx['object_list'] = request.GET.get('tag')
    #     return ctx
    #

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['object_3'] = BlogPost.objects.order_by('-id')[:3]
        ctx['tags'] = Tag.objects.all()
        return ctx


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
