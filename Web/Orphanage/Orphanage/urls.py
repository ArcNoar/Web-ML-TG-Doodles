
from django.contrib import admin
from django.urls import path

from Asiya.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Asiya/', include('Asiya.urls'))
]
