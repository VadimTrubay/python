from django.urls import path, include
from django.conf import settings
from user.views import *


urlpatterns = [
    path('sign-up/', UserRegistrationView.as_view(), name='register'),
    path('sign-in/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailView.as_view(), name='profile details'),
        path('edit/', EditProfileView.as_view(), name='edit profile'),
        path('delete/', DeleteProfileView.as_view(), name='delete profile'),
    ])),
]