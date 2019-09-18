from django.db import models

# Create your models here.

class Destination(models.Model):
    #id: models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    offertype= models.BooleanField(default=False)

class Menus(models.Model):
    menuname = models .CharField(max_length=200)
    menulink=models.TextField()


class Testimonials(models.Model):
    comment=models.CharField(max_length=200)
    name=models.CharField(max_length=20)
    position=models.CharField(max_length=20)

class News(models.Model):
    date=models.DateField(auto_now_add=True)
    title=models.CharField(max_length=35)
    description=models.CharField(max_length=100)
    tags=models.CharField(max_length=35)
    image = models.ImageField(upload_to='pics')

    