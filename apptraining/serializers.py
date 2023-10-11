from rest_framework import serializers

from apptraining.models import Course, Lesson, payment


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializers( serializers.ModelSerializer ):
    count_lesson = serializers.IntegerField(source='lesson_set.count')
    lesson = LessonSerializers(source='lesson_set', many=True)
    class Meta:
        model = Course
        fields = '__all__'

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