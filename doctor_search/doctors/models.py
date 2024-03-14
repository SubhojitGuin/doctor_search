from django.db import models
from accounts.models import User
from django.utils.functional import lazy

# Create your models here.
SPECIALITY_CHOICES = (
    ('Cardiologist', 'Cardiologist'),
    ('Dermatologist', 'Dermatologist'),
    ('Diabetologist', 'Diabetologist'),
    ('Dietitian', 'Dietitian'),
    ('Endocrinologist', 'Endocrinologist'),
    ('Gastroenterologist', 'Gastroenterologist'),
    ('Gynecologist', 'Gynecologist'),
    ('Hematologist', 'Hematologist'),
    ('Neurologist', 'Neurologist'),
    ('Oncologist', 'Oncologist'),
    ('Ophthalmologist', 'Ophthalmologist'),
    ('Pediatrician', 'Pediatrician'),
    ('Psychiatrist', 'Psychiatrist'),
    ('Pulmonologist', 'Pulmonologist'),
    ('Rheumatologist', 'Rheumatologist'),
    ('Urologist', 'Urologist'),
    ('Other', 'Other'),
)

# DAYS_CHOICES = (
#     ('Monday', 'Monday'),
#     ('Tuesday', 'Tuesday'),
#     ('Wednesday', 'Wednesday'),
#     ('Thursday', 'Thursday'),
#     ('Friday', 'Friday'),
#     ('Saturday', 'Saturday'),
#     ('Sunday', 'Sunday'),
# )


# class Day(models.Model):
#     day = models.CharField(max_length=10, choices=DAYS_CHOICES, unique=True)
#
#     def __str__(self):
#         return self.day
#
# DAY_CHOICES = lazy(Day.objects.all, list)()

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    specialty = models.CharField(max_length=100, choices=SPECIALITY_CHOICES, default='Cardiologist')
    fees = models.IntegerField(default=0)
    # days = models.ManyToManyField('Day', choices=DAYS_CHOICES, null=True, blank=True)
    monday_start_time = models.TimeField(null=True, blank=True)
    monday_end_time = models.TimeField(null=True, blank=True)
    tuesday_start_time = models.TimeField(null=True, blank=True)
    tuesday_end_time = models.TimeField(null=True, blank=True)
    wednesday_start_time = models.TimeField(null=True, blank=True)
    wednesday_end_time = models.TimeField(null=True, blank=True)
    thursday_start_time = models.TimeField(null=True, blank=True)
    thursday_end_time = models.TimeField(null=True, blank=True)
    friday_start_time = models.TimeField(null=True, blank=True)
    friday_end_time = models.TimeField(null=True, blank=True)
    saturday_start_time = models.TimeField(null=True, blank=True)
    saturday_end_time = models.TimeField(null=True, blank=True)
    sunday_start_time = models.TimeField(null=True, blank=True)
    sunday_end_time = models.TimeField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')), default='M')
    education = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


