from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('me/', include('authapp.urls', namespace='authapp')),
    path('', include('links.urls', namespace='links')),
    path('admin/', admin.site.urls),
]