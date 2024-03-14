# Generated by Django 5.0.2 on 2024-02-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_alter_doctor_specialty_alter_doctor_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologist', 'Dermatologist'), ('Diabetologist', 'Diabetologist'), ('Dietitian', 'Dietitian'), ('Endocrinologist', 'Endocrinologist'), ('Gastroenterologist', 'Gastroenterologist'), ('Gynecologist', 'Gynecologist'), ('Hematologist', 'Hematologist'), ('Neurologist', 'Neurologist'), ('Oncologist', 'Oncologist'), ('Ophthalmologist', 'Ophthalmologist'), ('Pediatrician', 'Pediatrician'), ('Psychiatrist', 'Psychiatrist'), ('Pulmonologist', 'Pulmonologist'), ('Rheumatologist', 'Rheumatologist'), ('Urologist', 'Urologist'), ('Other', 'Other')], default='Cardiologist', max_length=100),
        ),
    ]