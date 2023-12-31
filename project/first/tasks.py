#from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from project import settings

# # yser id al
# @shared_task(bind=True)
# def send_mail_func(self, user_pk):
#     # operations
#     # user idden mail al
#     users = get_user_model().objects.all()

#     for user in users:
#         mail_subject = "Hye from celery"
#         message = "Yaaaa....I have completed this task by celery!!"
#         to_email = user.email
#         send_mail(
#             subject=mail_subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[to_email],
#             fail_silently=False,
#         )
#     return "Done"


@shared_task(bind=True)
def send_notification_mail(self, target_mail):
    mail_subject = "Welcome on Board!"
    message = "You just signed-up!"
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[target_mail],
        fail_silently=False,
    )
    return "Done"
