from django.db import models

# Create your models here.
class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('', 'Select Specialization'),
        ('Cardiologist', 'Cardiologist'),
        ('Dentist', 'Dentist'),
        ('Neurologist', 'Neurologist'),
        ('Orthopedic', 'Orthopedic'),
        ('Dermatologist', 'Dermatologist'),
    ]
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100,choices=SPECIALIZATION_CHOICES)
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.name