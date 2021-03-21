from django.contrib import admin
from django.urls import include, path
from django.views.defaults import page_not_found

urlpatterns = [
    path('404/', page_not_found, {'exception': Exception()}),
    path('me/', include('allauth.urls')),
    path('me/', include('authapp.urls', namespace='authapp')),
    path('', include('links.urls', namespace='links')),
    path('admin/', admin.site.urls),
]