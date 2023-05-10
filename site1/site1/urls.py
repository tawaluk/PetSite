from django.contrib import admin
from django.contrib import auth
from django.urls import path, include
from infoposts import views

urlpatterns = [
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('infoposts.urls', namespace='infoposts')),
]
