from django.contrib.auth import login
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *
from .forms import *


class MainView(View):

    def get(self, request, *args, **kwargs):
        workouts = WorkoutPost.objects.all()
        posts = ContentPost.objects.all()

        paginator_workout = Paginator(workouts, 3)
        paginator_post = Paginator(posts, 3)

        page_number_w = request.GET.get('page_w')
        page_number_p = request.GET.get('page_p')
        page_obj_work = paginator_workout.get_page(page_number_w)
        page_obj_post = paginator_post.get_page(page_number_p)

        return render(request, 'blog_app/index.html', context={
            'page_obj_work': page_obj_work,
            'page_obj_post': page_obj_post,
        })


class WorkDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        work = get_object_or_404(WorkoutPost, slug=slug)
        return render(request, 'blog_app/detail_work.html', context={'work': work})


class PostDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(ContentPost, slug=slug)
        return render(request, 'blog_app/detail_post.html', context={'post': post})


class RegistView(View):

    def get(self, request, *args, **kwargs):
        form = RegistForm()
        return render(request, 'blog_app/regist.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = RegistForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'blog_app/regist.html', context={
            'form': form,
        })


class AuthView(View):

    def get(self, request, *args, **kwargs):
        form = AuthForm()
        return render(request, 'blog_app/login.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = AuthForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'blog_app/login.html', context={
            'form': form,
        })


class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'blog_app/contact.html', context={
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'От {name} | {subject}', message, from_email, ['yourgymnastic@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок!')
            return HttpResponseRedirect('success')
        return render(request, 'blog_app/contact.html', context={
            'form': form,
        })


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog_app/thanks.html', context={
            'title': 'Спасибо',
        })