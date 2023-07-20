from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from first.serializers import UserSerializer

# defines a Django ViewSet for the User model
class UserViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
