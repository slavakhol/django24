
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from main.apps import MainConfig
from main.views import CourseViewSet, LessonCreateAPIView, LessonUpdateAPIView, LessonRetrieveAPIView, \
    LessonListAPIView, LessonDestroyAPIView, PaymentListAPIView, SubscriptionCreateView, SubscriptionDeleteView

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

app_name = MainConfig.name
urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name="lesson_create"),
    path('lesson/', LessonListAPIView.as_view(), name="lesson_list"),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name="lesson_update"),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name="lesson_delete"),

    path('payment/', PaymentListAPIView.as_view(), name="payment_list"),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('subscription/create/', SubscriptionCreateView.as_view(), name='subcription_create'),
    path('subscription/delete/<int:pk>/', SubscriptionDeleteView.as_view(), name='subcription_delete'),


              ] + router.urls