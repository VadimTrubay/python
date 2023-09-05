from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from .models import Order, Product, OrderItem
from .forms import OrderForm, OrderItemForm
from django.views.generic import ListView, CreateView, TemplateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from utils.utils import DataMixin
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q


class HomePage(DataMixin, TemplateView):
    template_name = 'order/home_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='контакты')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context


class AddOrder(DataMixin, CreateView):
    form_class = OrderForm
    template_name = 'order/add_order.html'
    success_url = reverse_lazy('all_orders')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='+ добавить новый заказ')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context


class ViewOrder(DataMixin, DetailView):
    model = Order
    template_name = 'order/view_order.html'
    context_object_name = 'order'
    success_url = reverse_lazy('all_orders')

    def get_queryset(self):
        if self.request.user.username == 'admin':
            object_list = self.model.objects.all().reverse()
        else:
            object_list = self.model.objects.filter(user=self.request.user).reverse()
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='просмотр заказа')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context


class AllOrders(DataMixin, ListView):
    paginate_by = 10
    model = Order
    template_name = 'order/all_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        if self.request.user.username == 'admin':
            object_list = self.model.objects.all().reverse()
        else:
            object_list = self.model.objects.filter(user=self.request.user).reverse()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='заказы')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context


class EditOrder(DataMixin, UpdateView):
    form_class = OrderForm
    template_name = 'order/edit_order.html'
    context_object_name = 'order'

    def get_success_url(self):
        referer = self.request.session.get('previous_url')  # Получаем предыдущий URL-адрес из сессии
        if referer:
            return referer
        return reverse_lazy('all_orders')

    def get(self, request, *args, **kwargs):
        previous_url = self.request.META.get('HTTP_REFERER')
        self.request.session['previous_url'] = previous_url
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='изменить заказ')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Order, pk=pk)


class EditItemProduct(DataMixin, UpdateView):
    form_class = OrderItemForm
    template_name = 'order/edit_item_product.html'
    context_object_name = 'order'
    success_url = reverse_lazy('all_orders')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(OrderItem, pk=pk)

    def get_success_url(self):
        order_id = self.object.order.id
        return reverse('view_order', kwargs={'pk': order_id})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='изменить продукт')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context


class DeleteOrder(DataMixin, DeleteView):
    model = Order
    template_name = 'order/delete_order.html'
    success_url = reverse_lazy('all_orders')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='удалить заказ')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context


class DeleteItemProduct(DataMixin, DeleteView):
    model = OrderItem
    template_name = 'order/delete_item_product.html'
    success_url = reverse_lazy('all_orders')

    def get_success_url(self):
        order_id = self.object.order.id
        return reverse('view_order', kwargs={'pk': order_id})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='удалить продукт')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context


class AddItem(DataMixin, CreateView):
    form_class = OrderItemForm
    template_name = 'order/add_item.html'
    success_url = reverse_lazy('all_orders')

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        order = Order.objects.get(pk=pk, user=self.request.user, done=False)
        form.instance.order = order
        return super().form_valid(form)

    def get_success_url(self):
        order_id = self.object.order.id
        return reverse('view_order', kwargs={'pk': order_id})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='добавить новый продукт в заказ')
        context = dict(list(context.items()) + list(context_menu.items()))
        return context


class SearchResultsOrder(DataMixin, ListView):
    model = Order
    template_name = 'order/search_results_order.html'
    context_object_name = 'orders'

    def get_queryset(self):
        query = self.request.GET.get('search_order')
        if self.request.user.username == 'admin':
            if query:
                queryset = self.model.objects.all().filter(
                    Q(user__username__icontains=query) |
                    Q(created_at__day__icontains=query) |
                    Q(done__icontains=query) |
                    Q(products__product__icontains=query)).reverse()
                return queryset
            return self.model.objects.none()
        else:
            user_orders = self.model.objects.filter(user=self.request.user)
            if query:
                queryset = user_orders.filter(
                    Q(user__username__icontains=query) |
                    Q(created_at__day__icontains=query) |
                    Q(done__icontains=query) |
                    Q(products__product__icontains=query)).reverse()
                return queryset
            return self.model.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_menu = self.get_menu_context(title='результаты поиска заказа')
        context.update(context_menu)
        return context
