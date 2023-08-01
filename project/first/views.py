from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.http import HttpResponse

# from first.tasks import send_mail_func
from first.tasks import send_notification_mail

from first.serializers import UserSerializer


# defines a Django ViewSet for the User model
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            user_email = user.email

            send_notification_mail.delay(user_email)
            return HttpResponse("Sent Email Successfully...Check your mail please")

        else:
            return HttpResponse(serializer.errors, status=400)

    # def send_mail_to_all(request):
