from datetime import datetime

menu = [
    {'title': 'продукты', 'url_name': 'all_products'},
    {'title': 'заказы', 'url_name': 'all_orders'}
]


class DataMixin:

    def get_menu_context(self, **kwargs):
        current_date = datetime.now().strftime('%d %B %Y')
        context = kwargs
        context['menu'] = menu
        context['current_date'] = current_date
        return context
