from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serialisers import UserSerialiser


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser