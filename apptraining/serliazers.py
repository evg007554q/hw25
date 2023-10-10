# from rest_framework import serializers
from rest_framework import serializers

from apptraining.models import Course


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
