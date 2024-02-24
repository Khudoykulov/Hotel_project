from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView
from .models import ServicesPost, Category
from .form import Comments, CommentForm
from django.contrib import messages


class ServicesListView(ListView):
    paginate_by = 3
    queryset = ServicesPost.objects.all()
    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt['services_3'] = ServicesPost.objects.order_by('-id')[:3]
        cnt['categories'] = Category.objects.all()
        return cnt

    template_name = 'services/service_list.html'


def service_detail(request, slug):
    service_3 = ServicesPost.objects.order_by('-id')[:3]
    blog = get_object_or_404(ServicesPost, slug=slug)
    categories = Category.objects.all()
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
        'service_3': service_3,
        'categories': categories,
        'comments': comments,
        'form': form

    }
    return render(request, 'services/service_detail.html', context)
