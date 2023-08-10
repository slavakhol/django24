from django.conf.urls.static import static
from django.urls import path
from rest_framework.routers import DefaultRouter
from main.apps import MainConfig
from main.views import CourseViewSet, LessonCreateAPIView, LessonUpdateAPIView, LessonRetrieveAPIView, \
    LessonListAPIView, LessonDestroyAPIView

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

app_name = MainConfig.name
urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name="lesson_create"),
    path('lesson/', LessonListAPIView.as_view(), name="lesson_list"),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name="lesson_update"),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name="lesson_delete"),

              ] + router.urls