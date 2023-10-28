from .models import Product
from .forms import ProductForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from utils.utils import DataMixin
from django.db.models import Q


class AddProduct(DataMixin, CreateView):
    form_class = ProductForm
    template_name = 'product/add_product.html'
    success_url = reverse_lazy('all_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='добавить новый продукт')
        context = dict(list(context.items()) + list(context_menu.items()))
        # context = context | context_menu
        return context


class AllProducts(DataMixin, ListView):
    paginate_by = 10
    model = Product
    template_name = 'product/all_products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='продукты')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context


class DeleteProduct(DataMixin, DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('all_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='удалить продукт')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context


class EditProduct(DataMixin, UpdateView):
    model = Product
    fields = ['product', 'price']
    template_name = 'product/edit_product.html'
    success_url = reverse_lazy('all_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='изменить продукт')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context


class SearchResultsProduct(DataMixin, ListView):
    model = Product
    template_name = 'product/search_results_product.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('search_product')
        if query:
            queryset = self.model.objects.filter(
                Q(product__icontains=query) |
                Q(price__icontains=query)
            )
            return queryset
        return self.model.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='результаты поиска продукта')
        context.update(context_menu)
        return context