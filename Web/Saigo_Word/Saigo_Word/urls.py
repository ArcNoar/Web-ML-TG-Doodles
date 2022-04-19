from django.contrib import admin
from django.urls import path, include

from Prima_Word.views import index

from django.conf.urls.static import static
from Saigo_Word import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Prima_Word/', include('Prima_Word.urls')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


