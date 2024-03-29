
from django.contrib import admin
from django.urls import path, include

from Asiya.views import index

from django.conf.urls.static import static
from Orphanage import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Asiya/', include('Asiya.urls')),
    path('__debug__/', include('debug_toolbar.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


