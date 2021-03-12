from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('authapp.urls', namespace='authapp')),
    path('admin/', admin.site.urls),
]