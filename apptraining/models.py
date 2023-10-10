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
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='категория', null=True, blank=True)

    image = models.ImageField(upload_to='image_apptraining/', verbose_name='Превью', null=True, blank=True)

    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', null=True, blank=True)
    last_modified_date = models.DateTimeField(auto_now_add=True, verbose_name='дата последнего изменения', null=True,
                                              blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Создатель')

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('name',)