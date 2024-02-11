from django.db import models
from ckeditor.fields import RichTextField
from apps.main.models import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Content(models.Model):
    content = RichTextField()
    quote = models.BooleanField(default=False)


class BlogPost(BaseModel):
    name = models.CharField(max_length=123)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='blog_content')
    image = models.ImageField(upload_to='media/',)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_category')
    tags = models.ManyToManyField(Tag, related_name='blog_tag')

    def __str__(self):
        return self.name

