from audioop import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from apptraining.models import Course, Lesson
from users.models import User


# from django.contrib.auth import get_user_model
# User = get_user_model()


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        usertest = User.objects.create(
            email='test@test.test',
            first_name='test',
            last_name='test',
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        usertest.set_password('1')
        usertest.save()

        self.user = usertest

        # print(self.user)
        # print(usertest)


        self.course = Course.objects.create(
            name='test Course',
        )
        self.lesson = Lesson.objects.create(
            name='test Lesson',
        )
        self.date_of_creation = None
        self.last_modified_date = None

        # self.lesson.course.set([self.course])

    def test_get_list(self):
        """Список лекций"""

        response = self.client.get(
            '/course/'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )


        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.course.id, 'count_lesson': 0, 'lesson': [], 'name': 'test Course', 'description': None, 'image': None,
                 'date_of_creation': response.json()['results'][0]['date_of_creation'],
                 'last_modified_date': response.json()['results'][0]['last_modified_date'],
                 'owner': None}]}

        )

    def test_create_course(self):
        """добавление курса test"""
        self.client.force_authenticate(user=self.user)
        data = {
            "name": "test",
            "description": "1 test",
            # 'owner': self.user.id,
        }

        response = self.client.post(
            '/course/',
            data=data
        )

        print(response.json())
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 2, 'count_lesson': 0, 'lesson': [], 'name': 'test', 'description': '1 test', 'image': None,
             'date_of_creation': response.json()['date_of_creation'], 'last_modified_date': response.json()['last_modified_date'],
             'owner': 1}
        )



    def test_validation_course(self):
        """добавление курса test"""
        self.client.force_authenticate(user=self.user)
        data = {
            "name": "test https://colab.res",
            "description": "1 test",
            # 'owner': self.user.id,
        }

        response = self.client.post(
            '/course/',
            data=data
        )

        print(response.json())
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


