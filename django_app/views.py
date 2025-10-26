from django.shortcuts import render
from django.views.generic import ListView
from .models import django_app

class HomePageView(ListView):
    model = django_app
    template_name = 'home.html'
context_object_name = 'all_posts_list'