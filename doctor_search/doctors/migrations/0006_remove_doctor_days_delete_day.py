# Generated by Django 5.0.2 on 2024-02-18 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_alter_day_day_alter_doctor_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='days',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
    ]
