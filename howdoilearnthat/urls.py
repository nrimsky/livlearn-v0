from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('me/', include('allauth.urls')),
    path('me/', include('authapp.urls', namespace='authapp')),
    path('', include('links.urls', namespace='links')),
    path('admin/', admin.site.urls),
]