from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic as view

from .forms import RegistrationForm, LoginForm, EditProfileForm
from .models import SiteUser

UserModel = get_user_model()


def get_profile(pk):
    try:
        return UserModel.objects.get(pk=pk)
    except UserModel.DoesNotExist as ex:
        return None


class UserRegistrationView(view.CreateView):
    model = UserModel
    template_name = 'profile/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'profile/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class ProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, view.DetailView):
    model = SiteUser
    template_name = 'profile/profile-details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["is_owner"] = self.request.user == self.object

        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        profile = get_object_or_404(SiteUser, pk=pk)
        return profile

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')


class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, view.UpdateView):
    model = SiteUser
    form_class = EditProfileForm
    template_name = 'profile/edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object
        return context

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')


class DeleteProfileView(LoginRequiredMixin, UserPassesTestMixin, view.DeleteView):
    model = SiteUser
    template_name = 'profile/delete-profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        profile = get_object_or_404(SiteUser, pk=pk)
        return profile

    def get_success_url(self):
        return reverse_lazy('home')

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')


class UserLogOutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


