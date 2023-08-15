from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from main.models import User, Lesson, Course, Subscription


# Create your tests here.

class CourseTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@email.com', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_course(self):
        data = {
            "title": "Test",
            "description": "Course test"
        }
        response = self.client.post(
            '/course/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


class LessonTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@email.com', password='testpassword')
        self.client.force_authenticate(user=self.user)


    def test_lesson_create(self):
        """Тестирование создания урока"""
        data = {
            "title": "Test Lesson",
            "description": "Test Description",
            "link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }

        self.response = self.client.post('/lesson/create/', data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.get().title, 'Test Lesson')
        self.assertEqual(Lesson.objects.get().owner, self.user)

    def test_lesson_list(self):
        """Тестирование вывода списка уроков. Создаем еще одного пользователя модератор,
         присваиваем ем уодин из уроков и проверяем, что список выводит только те,
          что принадлежат user"""
        self.moderator = User.objects.create(email='moderator@email.com', password='testpassword')
        self.lessons = [
            Lesson.objects.create(
                owner=self.user,
                title='Test Lesson 1',
                description='Test Description 1',
                image='test1.jpg',
                link='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            ),
            Lesson.objects.create(
                owner=self.user,
                title='Test Lesson 2',
                description='Test Description 2',
                image='test2.jpg',
                link='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            ),
            Lesson.objects.create(
                owner=self.moderator,
                title='Test Lesson created by Moderator',
                description='Test Description 3',
                image='test3.jpg',
                link='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            )
        ]
        self.response = self.client.get('/lesson/')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(self.response.json().get('results')), 2)


    def test_lesson_update(self):
        """Тестирование обновления урока"""
        self.lesson = Lesson.objects.create(
            owner=self.user,
            title='Test Lesson',
            description='Test Description',
            link='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        )
        data = {
            "title": "Test Lesson Updated",
            "description": "Test Description Updated",
            "link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }
        self.response = self.client.put(f'/lesson/update/{self.lesson.pk}/', data)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.get().title, 'Test Lesson Updated')


    def test_lesson_retrieve(self):
        """Тестирование вывода одного урока"""
        self.lesson = Lesson.objects.create(
            owner=self.user,
            title='Test Lesson',
            description='Test Description',
            link='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        )

        self.response = self.client.get(f'/lesson/{self.lesson.pk}/')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.get().title, 'Test Lesson')

    def test_lesson_delete(self):
        """Тестирование удаления урока"""
        self.lesson = Lesson.objects.create(
            owner=self.user,
            title='Test Lesson',
            description='Test Description',
            link='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        )

        self.response = self.client.delete(f'/lesson/delete/{self.lesson.pk}/')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@email.com', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create (
            title="Test",
            description="Course test"
        )


    def test_subscription_create(self):
        """Тестирование создания подписки"""
        data = {
            "user": self.user.pk,
            "course": self.course.pk,
            "is_subscribed": True
        }

        self.response = self.client.post('/subscription/create/', data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_subscription_delete(self):
        """Тестирование создания подписки"""
        self.subscription = Subscription.objects.create (
            user=self.user,
            course=self.course,
            is_subscribed=True
        )

        self.response = self.client.delete(f'/subscription/delete/{self.subscription.pk}/')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
