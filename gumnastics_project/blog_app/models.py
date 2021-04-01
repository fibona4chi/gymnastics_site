from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ContentPost(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = RichTextUploadingField()
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='image/%Y/%m/%d/')
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.title
