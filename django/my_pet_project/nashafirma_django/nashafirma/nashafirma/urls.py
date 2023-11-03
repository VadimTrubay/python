from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from order.views import *


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', HomePage.as_view(), name='home'),
                  path('about/', About.as_view(), name='about'),
                  path('product/', include('product.urls')),
                  path('order/', include('order.urls')),
                  path('user/', include('user.urls')),
                  path('contacts/', Contacts.as_view(), name='contacts'),
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound