from celery import shared_task
from django.core.mail import send_mail

from apptraining.models import Course, Subscription
from config import settings


@shared_task()
def email_after_update(pk):
    instance = Course.objects.filter(pk=pk).first()

    if instance:
        for subscription in Subscription.objects.filter(course=pk):
            # print(f'{subscription.user.email} Обновился курс -{instance.name} Описание {instance.description} - {instance.video_url}')
            send_mail(subject=f'Обновился курс -{instance.name} ', message=f'Описание {instance.description} - {instance.video_url}',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[subscription.user.email]
                      )
