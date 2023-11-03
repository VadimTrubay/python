from django.db import models
from django.urls import reverse
from product.models import Product
from datetime import datetime, timedelta
from user.models import SiteUser


class Order(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name='создан')
    user = models.ForeignKey(SiteUser, blank=True, null=True, on_delete=models.CASCADE, verbose_name='заказчик')
    products = models.ManyToManyField(Product, through='OrderItem', verbose_name='продукты')
    done = models.BooleanField(default=False, verbose_name='выполнен')

    def __str__(self):
        formatted_date_time = self.created_at.strftime('%d %B %Y')
        return formatted_date_time

    def get_absolute_url(self):
        return reverse('view_order', kwargs={'pk': self.pk})

    def calculate_sum_weight(self):
        return sum(item.weight for item in self.orderitem_set.all())

    def calculate_sum_total(self):
        return round(sum(item.calculate_total() for item in self.orderitem_set.all()), 2)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказ'
        ordering = ['created_at', 'user', 'done']


class OrderItem(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE, verbose_name='дата заказа')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    weight = models.FloatField(default=0, blank=True, null=True, verbose_name='вес')
    note = models.CharField(max_length=100, blank=True, verbose_name='примечание')

    def __str__(self):
        return f"{self.order}"

    def get_absolute_url(self):
        return reverse('view_order', kwargs={'pk': self.pk})

    def calculate_total(self):
        return round(self.product.price * self.weight, 2)

    class Meta:
        verbose_name = 'продукты'
        verbose_name_plural = 'продукты'
        ordering = ['order', 'product', 'weight']