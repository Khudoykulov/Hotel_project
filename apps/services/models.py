from django.db import models
from ckeditor.fields import RichTextField
from apps.main.models import BaseModel
from django.utils.text import slugify
from django.utils import timezone
from django.db.models.signals import pre_save


class Tag(BaseModel):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class ServicesPost(BaseModel):
    name = models.CharField(max_length=123)
    image = models.ImageField(upload_to='media/', )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_category')
    tags = models.ManyToManyField(Tag, related_name='blog_tag', null=True, blank=True)
    slug = models.SlugField(unique=True,)

    def __str__(self):
        return self.name


class Content(BaseModel):
    blog = models.ForeignKey(ServicesPost, on_delete=models.CASCADE, related_name='content', )
    content = RichTextField()
    quote = models.BooleanField(default=False)


def blog_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name + " - " + timezone.now().date().strftime('%Y-%m-%d %H:%M:%S.%f'))


pre_save.connect(blog_pre_save, sender=ServicesPost)

