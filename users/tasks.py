from celery import shared_task
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


@shared_task()
def deactivate_inactive_users():
    users = User.objects.all()
    for user in users:
        if user.last_login:
            time_blok = timezone.now() - timezone.timedelta(days=30)
            if time_blok >= user.last_login :
                user.is_active = False
                user.save()