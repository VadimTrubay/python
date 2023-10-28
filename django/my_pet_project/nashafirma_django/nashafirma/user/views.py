from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from .forms import *
from .models import *
from utils.utils import DataMixin


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('all_orders')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='регистрация')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='авторизация')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
