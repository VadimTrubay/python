from django.urls import path
from order.views import *


urlpatterns = [
    path('add_order/', AddOrder.as_view(), name='add_order'),
    path('view_order/<int:pk>/', ViewOrder.as_view(), name='view_order'),
    path('all_orders/', AllOrders.as_view(), name='all_orders'),
    path('delete_order/<int:pk>/', DeleteOrder.as_view(), name='delete_order'),
    path('delete_item_product/<int:pk>/', DeleteItemProduct.as_view(), name='delete_item_product'),
    path('edit_item_product/<int:pk>/', EditItemProduct.as_view(), name='edit_item_product'),
    path('edit_order/<int:pk>/', EditOrder.as_view(), name='edit_order'),
    path('add_item/<int:pk>/', AddItem.as_view(), name='add_item'),
    path('search_order/', SearchResultsOrder.as_view(), name='search_results_order'),
]