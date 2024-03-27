# Create your models here.
from django.db import models


# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=30)
    building = models.CharField(max_length=30)
    floor = models.CharField(max_length=30)
    total = models.DecimalField(decimal_places=0, max_digits=2)
    remain = models.DecimalField(decimal_places=0, max_digits=2)
    date = models.DateField()
    time_create = models.TimeField()
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)  # ฟิลด์ใหม่สำหรับรูปภาพ
    
    class Meta:
        verbose_name_plural = "List of Rooms"

    def __str__(self):
        return self.room_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "List of Users"

    def __str__(self):
        return self.email
    


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    uid=models.DecimalField(decimal_places=0, max_digits=2)
    room_name = models.CharField(max_length=30)
    building = models.CharField(max_length=30)
    floor = models.CharField(max_length=30)
    total = models.DecimalField(decimal_places=0, max_digits=2)
    date = models.DateField()
    time_create = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)  # ฟิลด์ใหม่สำหรับรูปภาพ
    time_period = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name_plural = "List of Books"
    def __str__(self):
        return self.email
