from django.db import models


class RoomType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    number = models.IntegerField()
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.number} - {self.room_type.name}"
