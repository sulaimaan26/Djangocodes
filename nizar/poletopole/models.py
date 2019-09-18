from django.db import models

# Create your models here.

class Header(models.Model):
    header_menu=models.CharField(max_length=20)
    header_menu_link=models.CharField(max_length=20)

class HomepageBanner(models.Model):
    Banner_Image=models.ImageField(upload_to='pics/home')
    Banner_Heading=models.CharField(blank=True,max_length=9)
    Banner_Text=models.CharField(blank=True,max_length=22)

class HomepageDestination(models.Model):
    Destination_Title=models.CharField(blank=True,max_length=30)
    Destination_Message=models.CharField(blank=True,max_length=30)
    Destination_Image=models.ImageField(upload_to='pics/home')
    Destination_Price=models.IntegerField()
    Destination_Placename=models.CharField(max_length=20)
    Destination_link=models.CharField(blank=True,max_length=20)

class HomepageOffersection(models.Model):
    Background_Image=models.ImageField(upload_to='pics/home')
    First_Offer_Place=models.CharField(blank=True,max_length=10)
    First_Offer_Percentage=models.CharField(blank=True,max_length=10)
    First_Offer_Subject=models.CharField(blank=True,max_length=20)
    First_Offer_Description=models.CharField(blank=True,max_length=200)
    First_Button_Link=models.CharField(blank=True,max_length=10)
    
    Second_Offer_Place=models.CharField(blank=True,max_length=10)
    Second_Offer_Percentage=models.CharField(blank=True,max_length=10)
    Second_Offer_Subject=models.CharField(blank=True,max_length=20)
    Second_Offer_Description=models.CharField(blank=True,max_length=200)
    Second_Button_Link=models.CharField(blank=True,max_length=10)

    
class HomepageVideo(models.Model):
    Title=models.CharField(blank=True,max_length=50)
    Description=models.CharField(blank=True,max_length=50)
    Video_URL=models.CharField(blank=True,max_length=200)
    Background_Image=models.ImageField(blank=True)

class HomepagePopularDestionation(models.Model):
    Title=models.CharField(blank=True,max_length=50)
    Description=models.CharField(blank=True,max_length=50)
    Destination_Image=models.ImageField(upload_to='pics/home')
    Destination_Price=models.IntegerField()
    Destination_Placename=models.CharField(max_length=20)
    Pageurl=models.CharField(blank=True,max_length=50)


class HomepageSpecialOffers(models.Model):
    Title=models.CharField(blank=True,max_length=50)
    Description=models.CharField(blank=True,max_length=50)
    Destination_Image=models.ImageField(upload_to='pics/home')
    Destination_Subject=models.CharField(max_length=20)
    Destination_Placename=models.CharField(max_length=20)
    
    

