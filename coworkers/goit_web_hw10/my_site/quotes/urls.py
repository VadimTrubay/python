from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
#     path('', views.quote, name='quote'),
    path('', views.main, name='main'),
    path('<int:page>', views.main, name='main_paginate'),
    path('tag/', views.tag, name='tag'),
    path('quote/', views.quote, name='quote'),
    path('author/', views.author, name='author'),
    path('author_about/<int:pk>/', views.author_about, name='author_about'),
    path('tag_search/<int:_id>', views.tag_search, name='tag_search')
]
