from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User

from users.serializers import UsersSerializer


class UsersViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
