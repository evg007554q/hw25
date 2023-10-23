from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter

from apptraining.apps import ApptrainingConfig
from apptraining.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, Course_paymentListAPIView, Course_paymentCreateAPIView, GetPlamentView

app_name = ApptrainingConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'createpayment', Course_paymentCreateAPIView, basename='createpayment')


urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_cart'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    #payment
    path('Course/payment/', Course_paymentListAPIView.as_view(), name='Course_payment'),
    path('Course/pay/<str:payment_id>/', GetPlamentView.as_view(), name='Course_info_payment'),

              ] + router.urls
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
