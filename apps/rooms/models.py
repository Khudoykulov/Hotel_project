from ckeditor.fields import RichTextField
from django.db import models
from apps.main.models import BaseModel


class PriceRoom(models.Model):
    UNIT = (
        (1, '01'),
        (2, '02'),
        (3, '03'),
        (4, '04'),
        (5, '05'),
        (6, '06'),
    )
    price_min = models.IntegerField(default=0)
    price_max = models.IntegerField()
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.IntegerField(choices=UNIT, default='adults')
    children = models.IntegerField(choices=UNIT, default=2)


class RoomService(BaseModel):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='services_room')
    name = models.CharField(max_length=123)
    image = models.ImageField(upload_to='rooms/service/')


class RoomContent(BaseModel):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='content_room')
    content = RichTextField()
    chek = models.BooleanField(default=False)


class Room(BaseModel):
    name = models.CharField(max_length=123)
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to='rooms/', null=True, blank=True)
    max_persion = models.IntegerField(default=1)
    size_a = models.IntegerField()
    size_b = models.IntegerField()
    bed = models.CharField(max_length=123, null=True, blank=True)

    def __str__(self):
        return self.name
