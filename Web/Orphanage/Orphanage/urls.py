
from django.contrib import admin
from django.urls import path, include

from Asiya.views import index

from django.conf.urls.static import static
from Orphanage import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Asiya/', include('Asiya.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)