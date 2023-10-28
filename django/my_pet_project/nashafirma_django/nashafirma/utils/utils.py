from datetime import datetime

menu = [
    {'menu_name': 'Home', 'url_name': 'home'},
    {'menu_name': "About", 'url_name': 'about'},
    {'menu_name': "Products", 'url_name': 'all_products'},
    {'menu_name': "Orders", 'url_name': 'all_orders'},
    {'menu_name': "Contacts", 'url_name': 'contacts'},
]


class DataMixin:

    def get_menu_context(self, **kwargs):
        current_date = datetime.now().strftime('%d %B %Y')
        context = kwargs
        context['menu'] = menu
        context['current_date'] = current_date
        return context
