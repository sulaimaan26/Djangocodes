# Generated by Django 2.2.5 on 2019-09-17 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_menu', models.CharField(max_length=20)),
                ('header_menu_link', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Background_Image', models.ImageField(upload_to='pics/home')),
                ('Video_URL', models.CharField(blank=True, max_length=200)),
                ('Title2', models.CharField(max_length=30)),
                ('Title3', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HomepageBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Banner_Image', models.ImageField(upload_to='pics/home')),
                ('Banner_Heading', models.CharField(blank=True, max_length=9)),
                ('Banner_Text', models.CharField(blank=True, max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='HomepageDestination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destination_Title', models.CharField(blank=True, max_length=30)),
                ('Destination_Message', models.CharField(blank=True, max_length=30)),
                ('Destination_Image', models.ImageField(upload_to='pics/home')),
                ('Destination_Price', models.IntegerField()),
                ('Destination_Placename', models.CharField(max_length=20)),
                ('Destination_link', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HomepageOffersection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Background_Image', models.ImageField(upload_to='pics/home')),
                ('First_Offer_Place', models.CharField(blank=True, max_length=10)),
                ('First_Offer_Percentage', models.CharField(blank=True, max_length=10)),
                ('First_Offer_Subject', models.CharField(blank=True, max_length=20)),
                ('First_Offer_Description', models.CharField(blank=True, max_length=200)),
                ('First_Button_Link', models.CharField(blank=True, max_length=10)),
                ('Second_Offer_Place', models.CharField(blank=True, max_length=10)),
                ('Second_Offer_Percentage', models.CharField(blank=True, max_length=10)),
                ('Second_Offer_Subject', models.CharField(blank=True, max_length=20)),
                ('Second_Offer_Description', models.CharField(blank=True, max_length=200)),
                ('Second_Button_Link', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
