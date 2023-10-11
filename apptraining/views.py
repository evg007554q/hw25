
from rest_framework import viewsets, generics

from apptraining.models import Course, Lesson, payment
from apptraining.serializers import CourseSerializers, LessonSerializers, CoursepaymentSerializers

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from rest_framework.permissions import IsAuthenticated


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated]

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

class Course_paymentListAPIView(generics.ListAPIView):
    queryset = payment.objects.all()
                # .filter(cash=True))
    serializer_class = CoursepaymentSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'cash',)
    ordering_fields = ('date_of_payment',)
    permission_classes = [IsAuthenticated]


