from django.db import models

# Create your models here.


# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

      
class Room(models.Model):
  name = models.CharField(max_length=200)
  price = models.IntegerField()
  discount = models.IntegerField()
  image = models.ImageField(upload_to="rooms/image",)
  description = models.TextField()
  
  def __str__(self) -> str:
    return self.name
  

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()
    room_id = models.IntegerField()
    
    def __str__(self) -> str:
        return self.full_name  # Change this to full_name or another relevant field

    

