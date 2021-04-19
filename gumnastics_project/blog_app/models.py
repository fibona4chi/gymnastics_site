from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class WorkoutPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название тренировки')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    description = RichTextUploadingField(verbose_name='Начало контента')
    content = RichTextUploadingField(verbose_name='Продолжение контента')
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True, verbose_name='Фото/изображение')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тренировка(у)'
        verbose_name_plural = 'Тренировки'


class ContentPost(models.Model):
    h1 = models.CharField(max_length=200, verbose_name='Заголовок')
    title = models.CharField(max_length=200, verbose_name='Заголовок1')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    description = RichTextUploadingField(verbose_name='Начало контента')
    content = RichTextUploadingField(verbose_name='Продолжение контента')
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True, verbose_name='Фото/изображение')
    created_at = models.DateField(default=timezone.now, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя автроа поста')
    tag = models.ManyToManyField('Tag', blank=True, related_name='posts', verbose_name='Тэг')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', related_name='posts')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование тэга')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']