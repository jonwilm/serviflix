from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path, include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('apps.home.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.services.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'SERVIFLIX'
admin.site.index_title = 'Panel de Administración'
admin.site.site_title = 'Serviflix'
