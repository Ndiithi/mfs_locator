from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from mfs_locator.serializers import UserSerializer, GroupSerializer,LocatorSerializer

from locator.models import Locator

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows locator to be viewed or edited.
    """
    queryset = Locator.objects.all().order_by('-created')
    serializer_class = LocatorSerializer
    permission_classes = [permissions.IsAuthenticated]
