# Generated by Django 4.2.4 on 2023-08-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_lesson_options_course_payment_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='стоимость'),
        ),
    ]
