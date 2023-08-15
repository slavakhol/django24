from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=35, verbose_name="телефон")
    city = models.CharField(max_length=50, verbose_name="город")
    avatar = models.ImageField(upload_to="images/users", verbose_name="аватар")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Course(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name="название")
    description = models.CharField(max_length=200, verbose_name="описание")
    image = models.ImageField(upload_to="images/courses", null=True, blank=True, verbose_name="изображение")
    price = models.IntegerField(default=0, blank=True, null=True, verbose_name='стоимость')
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name="название")
    description = models.CharField(max_length=200, verbose_name="описание")
    image = models.ImageField(upload_to="images/courses", null=True, blank=True, verbose_name="изображение")
    link = models.URLField(null=True, blank=True, verbose_name="ссылка")
    course = models.ForeignKey(Course, verbose_name='курс',
                                on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ['title']

class Payment(models.Model):
    payment_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    payment_date = models.DateField(verbose_name="дата оплаты")
    payment_amount = models.IntegerField(verbose_name="сумма")
    payment_method = models.CharField(max_length=50, choices=[('cash', 'Наличные'), ('transfer', 'Перевод на счет')])
    paid_lesson = models.ForeignKey(
        Lesson, verbose_name='Оплаченный урок', on_delete=models.CASCADE,
        null=True, blank=True, related_name='paid_lesson',
    )
    paid_course = models.ForeignKey(
        Course, verbose_name='Оплаченный курс', on_delete=models.CASCADE,
        null=True, blank=True, related_name='paid_course',
    )

    def __str__(self):
        return f'{self.payment_date} - {self.payment_amount} - {self.payment_user}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'