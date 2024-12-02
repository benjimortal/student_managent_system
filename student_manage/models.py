from django.db import models

# Create your models here.

CHOICES = [
    ('CE', 'CE'),
    ('EXTC', 'EXTC'),
    ('ME', 'ME'),
    ('AI', 'AI'),
    ('IT', 'IT')
    ]
 
class Student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.PositiveIntegerField()
    branch = models.CharField(max_length=20, choices=CHOICES)
    
    
    def __str__(self):
        return f"{self.fname} {self.lname}"