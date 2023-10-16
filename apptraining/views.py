
from rest_framework import viewsets, generics

from apptraining.models import Course, Lesson, payment, Subscription
from apptraining.paginators import apptrainingPaginator
from apptraining.permissions import IsOwnerOrStaff, IsModerator, IsOwner, IsMember
from apptraining.serializers import CourseSerializers, LessonSerializers, CoursepaymentSerializers, \
    SubscriptionSerializers

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from rest_framework.permissions import IsAuthenticated


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator|IsOwner]
    pagination_class = apptrainingPaginator
    def perform_create(self, serializer_class):
        newL = serializer_class.save()
        newL.owner = self.request.user
        newL.save()




class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated, IsMember]
    #Авторизован и группа IsMember
    def perform_create(self, serializer_class):
        newL = serializer_class.save()
        newL.owner = self.request.user
        newL.save()

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator|IsOwner]
    pagination_class = apptrainingPaginator



class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator|IsOwner]

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()

    permission_classes = [IsAuthenticated, IsModerator|IsOwner]

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]





class Course_paymentListAPIView(generics.ListAPIView):
    queryset = payment.objects.all()
                # .filter(cash=True))
    serializer_class = CoursepaymentSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'cash',)
    ordering_fields = ('date_of_payment',)
    permission_classes = [IsAuthenticated, IsModerator|IsOwner]





class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializers
    permission_classes = [IsAuthenticated, IsMember]
    #Авторизован и группа IsMember
    def perform_create(self, serializer_class):
        newS = serializer_class.save()
        newS.owner = self.request.user
        newS.save()

class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionSerializers
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, IsModerator|IsOwner]

class SubscriptionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubscriptionSerializers
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, IsModerator|IsOwner]

class SubscriptionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SubscriptionSerializers
    queryset = Subscription.objects.all()

    permission_classes = [IsAuthenticated, IsModerator|IsOwner]

class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

