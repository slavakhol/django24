# Generated by Django 4.2.4 on 2023-08-12 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_payment_paid_course_alter_payment_paid_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='lessons',
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course', verbose_name='уроки'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='ссылка'),
        ),
    ]
