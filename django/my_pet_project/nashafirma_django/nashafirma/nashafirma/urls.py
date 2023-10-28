from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from order.views import pageNotFound


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('order.urls')),
                  path('', include('product.urls')),
                  path('', include('user.urls')),
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound