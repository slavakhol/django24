from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters

from main.models import Course, Lesson, Payment, Subscription
from main.paginators import MaterialPaginator
from main.permissions import IsOwner, IsModerator, NotModerator
from main.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer
from main.tasks import course_update_mail


class CourseViewSet(viewsets.ModelViewSet):
    '''ViewSet для модели Курс'''
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MaterialPaginator

    def perform_update(self, serializer):
        updated_course = serializer.save()
        course_update_mail(updated_course)

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action in [ 'retrieve', 'destroy']:
            permission_classes = [IsOwner]
        elif self.action in ['list']:
            permission_classes = [IsModerator]
        else:
            permission_classes = [NotModerator]
        return [permission() for permission in permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    '''Отображение для создания Урока'''
    serializer_class = LessonSerializer
    permission_classes = [NotModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    '''Отображение для вывода списка Уроков'''
    serializer_class = LessonSerializer
    pagination_class = MaterialPaginator

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name__exact="Moderator").exists():
            return Lesson.objects.all()

        return Lesson.objects.filter(owner=user)

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    '''Отображение для вывода информации по одному Уроку'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    '''Отображение для обновления Урока'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    '''Отображение для удаления Урока'''
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class PaymentListAPIView(generics.ListAPIView):
    '''Отображение для вывода списка платежей'''
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('paid_lesson', 'paid_course', 'payment_method')
    ordering_fields = ['payment_date']


class SubscriptionCreateView(generics.CreateAPIView):
    '''Отображение для создания Подписки'''
    serializer_class = SubscriptionSerializer

class SubscriptionDeleteView(generics.DestroyAPIView):
    '''Отображение для удаления Подписки'''
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()