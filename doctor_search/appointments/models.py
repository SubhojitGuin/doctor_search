from django.db import models
from accounts.models import User
from doctors.models import Doctor


# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.doctor.name} - {self.patient.username} - {self.date} {self.start_time}"


class AppointmentRequest(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return f"{self.doctor.name} - {self.patient.username} - {self.date} {self.start_time} - {self.status}"


class TemporaryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
