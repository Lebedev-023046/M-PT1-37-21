from django.db import models

# Create your models here.

class Element(models.Model):

    Producer_Name = models.CharField("Producer_Name", max_length=30, blank=False, default='')
    title = models.TextField("Description", default="")
    size = models.CharField("Size", max_length=5, blank=False)
    color = models.CharField("Color", max_length=20)
    structure = models.CharField("Structure", max_length=100)
    price = models.CharField("Price($)", max_length=50, blank=False)
    image = models.ImageField("Photo")


    def __str__(self):
        return self.price
