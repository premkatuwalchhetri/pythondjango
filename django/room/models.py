from django.db import models

# Create your models here.

class Room(models.Model):
  name = models.CharField(max_length=200)
  price = models.IntegerField()
  discount = models.IntegerField()
  image = models.ImageField(upload_to="rooms/image",)
  description = models.TextField()
  
  def __str__(self) -> str:
    return self.name
  