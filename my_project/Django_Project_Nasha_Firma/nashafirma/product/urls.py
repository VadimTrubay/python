from django.urls import path
from product.views import *


urlpatterns = [
    path('add_product/', AddProduct.as_view(), name='add_product'),
    path('all_products/', AllProducts.as_view(), name='all_products'),
    path('delete_product/<int:pk>/', DeleteProduct.as_view(), name='delete_product'),
    path('edit_product/<int:pk>/', EditProduct.as_view(), name='edit_product'),
    path('search_product/', SearchResultsProduct.as_view(), name='search_results_product'),
]