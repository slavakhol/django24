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
    title = models.CharField(max_length=50, verbose_name="название")
    description = models.CharField(max_length=200, verbose_name="описание")
    image = models.ImageField(upload_to="images/courses", verbose_name="изображение")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name="название")
    description = models.CharField(max_length=200, verbose_name="описание")
    image = models.ImageField(upload_to="images/courses", verbose_name="изображение")
    link = models.URLField( verbose_name="ссылка")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"