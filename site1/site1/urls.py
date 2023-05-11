from django.contrib import admin
from django.contrib import auth
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('infoposts.urls', namespace='infoposts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)