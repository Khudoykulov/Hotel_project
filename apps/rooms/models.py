from ckeditor.fields import RichTextField
from django.db import models
from apps.main.models import BaseModel
from django.utils.text import slugify
from django.utils import timezone
from django.db.models.signals import pre_save


class Room(BaseModel):
    name = models.CharField(max_length=123)
    price = models.IntegerField(default=100)
    max_person = models.IntegerField(default=1)
    size_a = models.IntegerField()
    size_b = models.IntegerField()
    bed = models.CharField(max_length=123, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Image(BaseModel):
    image = models.ImageField(upload_to='rooms/',)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_image')


class RoomContent(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='content_room')
    content = RichTextField()
    chek = models.BooleanField(default=False)


class RoomService(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='services_room')
    name = models.CharField(max_length=123)
    image = models.ImageField(upload_to='rooms/service/')


# class PriceRoom(models.Model):
#     UNIT = (
#         (0, '0'),
#         (1, '01'),
#         (2, '02'),
#         (3, '03'),
#         (4, '04'),
#         (5, '05'),
#         (6, '06'),
#     )
#     price_min = models.IntegerField(default=0)
#     price_max = models.IntegerField()
#     check_in = models.DateField()
#     check_out = models.DateField()
#     adults = models.IntegerField(choices=UNIT, default=2)
#     children = models.IntegerField(choices=UNIT, default=2)
#
#     class Meta:
#         abstract = True


class Booking(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='booking')
    # author = models.ForeignKey(auth.User, on_delete=models.SET_NULL, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.IntegerField()
    children = models.IntegerField()
    price_min = models.IntegerField(default=0)
    price_max = models.IntegerField()

    def __str__(self):
        return self.check_in

    # @property
    # def amount(self):
    #     pass


def blog_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name + " - " + timezone.now().date().strftime('%Y-%m-%d %H:%M:%S.%f'))


pre_save.connect(blog_pre_save, sender=Room)




