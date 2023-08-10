# Generated by Django 4.2.4 on 2023-08-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('description', models.CharField(max_length=200, verbose_name='описание')),
                ('image', models.ImageField(upload_to='images/courses', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('description', models.CharField(max_length=200, verbose_name='описание')),
                ('image', models.ImageField(upload_to='images/courses', verbose_name='изображение')),
                ('link', models.URLField(verbose_name='ссылка')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]