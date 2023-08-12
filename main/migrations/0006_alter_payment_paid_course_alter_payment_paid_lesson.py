# Generated by Django 4.2.4 on 2023-08-12 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_course_options_alter_lesson_options_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paid_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paid_course', to='main.course', verbose_name='Оплаченный курс'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paid_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paid_lesson', to='main.lesson', verbose_name='Оплаченный урок'),
        ),
    ]
