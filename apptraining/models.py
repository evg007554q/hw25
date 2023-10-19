from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Course(models.Model):
    """Курсы обучения"""
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=250, verbose_name='Описание курса', null=True, blank=True)
    image = models.ImageField(upload_to='image_apptraining/', verbose_name='Превью', null=True, blank=True)

    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', null=True, blank=True)
    last_modified_date = models.DateTimeField(auto_now_add=True, verbose_name='дата последнего изменения', null=True,
                                              blank=True)

    video_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на видео')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Создатель')

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('name',)


class Lesson(models.Model):
    """Урок"""
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=250, verbose_name='Описание урока', null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='курс', null=True, blank=True)

    image = models.ImageField(upload_to='image_apptraining/', verbose_name='Превью', null=True, blank=True)

    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', null=True, blank=True)
    last_modified_date = models.DateTimeField(auto_now_add=True, verbose_name='дата последнего изменения', null=True,
                                              blank=True)
    video_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на видео')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Создатель')

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('name',)



class payment(models.Model):
    """Оплата"""
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='оплаченый курс', null=True, blank=True)
    cash = models.BooleanField(default=True, verbose_name='Наличные')
    Payment_amount = models.IntegerField(default=0, verbose_name='Сумма оплаты')
    date_of_payment = models.DateTimeField(auto_now_add=True, verbose_name='дата оплата', null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Создатель')

    def __str__(self):
        return f'{self.owner} - {self.date_of_payment} '

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
        ordering = ('date_of_payment',)



class Subscription(models.Model):
    """подписка на обновление"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='user')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='курс', null=True, blank=True)

    def __str__(self):
        return f'{self.user} -{self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        ordering = 'course',