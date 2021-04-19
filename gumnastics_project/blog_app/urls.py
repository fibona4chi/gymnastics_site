from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('work/<str:slug>/', WorkDetailView.as_view(), name='work_detail'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('regist/', RegistView.as_view(), name='regist'),
    path('login/', AuthView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
]

