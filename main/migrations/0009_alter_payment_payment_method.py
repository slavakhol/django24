# Generated by Django 4.2.4 on 2023-08-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_lesson_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Наличные'), ('transfer', 'Перевод на счет')], max_length=50),
        ),
    ]
