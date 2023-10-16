from rest_framework import serializers

from apptraining.models import Course, Lesson, payment, Subscription
from apptraining.validators import urlValidator


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [urlValidator(field='name')]
        validatorsdescription = [urlValidator(field='description')]


class CourseSerializers( serializers.ModelSerializer ):
    count_lesson = serializers.IntegerField(source='lesson_set.count',read_only=True)
    lesson = LessonSerializers(source='lesson_set', many=True,read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
        validators = [urlValidator(field='name')]
        validatorsdescription = [urlValidator(field='description')]

class CourseShSerializers( serializers.ModelSerializer ):
    """Коротко о курсе"""
    # count_lesson = serializers.IntegerField(source='lesson_set.count')
    # lesson = LessonSerializers(source='lesson_set', many=True)
    class Meta:
        model = Course
        fields = ('name', 'id', )

class CoursepaymentSerializers(serializers.ModelSerializer):
    course = CourseShSerializers()
    class Meta:
        model = payment
        fields = '__all__'


class SubscriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


