from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from first.tasks import send_mail_func

from first.serializers import UserSerializer


# defines a Django ViewSet for the User model
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent Email Successfully...Check your mail please")
