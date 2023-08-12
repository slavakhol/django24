from django.core.management.base import BaseCommand
from datetime import date
from main.models import Payment, User, Course, Lesson


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment_user = input("Введите ID пользователя: ")
        payment_date = input("Введите дату оплаты (в формате ГГГГ-ММ-ДД): ")
        paid_lesson = input("Введите id оплаченного урока или остаьвте пустым: ")
        if paid_lesson == "":
            paid_lesson = None
        else:
            paid_lesson = Lesson.objects.get(id=paid_lesson)

        paid_course = input("Введите id оплаченного курса или остаьвте пустым: ")
        if paid_course == "":
            paid_course = None
        else:
            paid_course = Course.objects.get(id=paid_course)
        payment_amount = input("Введите сумму оплаты: ")
        payment_method = input("Введите способ оплаты (cash/transfer): ")

        payment = Payment(payment_user=User.objects.get(email=payment_user), payment_date=payment_date,
                          paid_lesson=paid_lesson, paid_course=paid_course,
                          payment_amount=payment_amount, payment_method=payment_method)
        payment.save()
        print("Новая запись добавлена в модель Payment.")
