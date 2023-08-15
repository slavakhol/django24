from rest_framework import serializers

from main.models import Course, Lesson, Payment, Subscription
from main.services import stripe_get_link
from main.validators import YoutubeValidator

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [YoutubeValidator(field='link')]

class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)
    user_is_subscribed = serializers.SerializerMethodField()
    payment_link = serializers.SerializerMethodField()
    def get_lessons_count(self, obj):
        return obj.lesson_set.count()

    def get_user_is_subscribed(self, obj):
        user = self.context['request'].user
        return obj.subscription_set.filter(user=user).exists()
    def get_payment_link(self, obj):
        return stripe_get_link(obj)

    class Meta:
        model = Course
        fields = "__all__"



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

