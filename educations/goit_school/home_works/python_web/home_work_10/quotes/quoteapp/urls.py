from django.urls import path
from . import views


app_name = 'quoteapp'

urlpatterns = [
    path('<int:page>', views.main, name="root_paginate"),
    path('tag/', views.tag, name='tag'),
    path('quote/', views.quote, name='quote'),
    path('author/', views.author, name='author'),
    path('detail/<int:author_id>', views.detail, name='detail'),
    path('tag_search/<int:tag_id>', views.tag_search, name='tag_search')
]


