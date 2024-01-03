from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from quoteapp.views import main


urlpatterns = [
                  path("admin/", admin.site.urls),
                  path('', main, name='main'),
                  path("quotes/", include("quoteapp.urls")),
                  path("users/", include("users.urls")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
