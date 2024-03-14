# Generated by Django 5.0.2 on 2024-02-19 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0007_alter_doctor_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='start_time',
        ),
        migrations.AddField(
            model_name='doctor',
            name='friday_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='friday_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='monday_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='monday_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='saturday_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='saturday_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='sunday_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='sunday_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='thursday_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='thursday_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='tuesday_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='tuesday_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='wednesday_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='wednesday_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]