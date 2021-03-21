from django.urls import include, path
from authapp.views import dashboard, privacy
from django.contrib.auth.decorators import login_required
# https://django-allauth.readthedocs.io/en/latest/forms.html

app_name = 'authapp'

urlpatterns = [
    path('privacy/', privacy, name='privacy'),
    path('dashboard/', dashboard, name='dashboard'),
]