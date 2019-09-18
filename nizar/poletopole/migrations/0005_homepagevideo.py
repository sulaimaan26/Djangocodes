# Generated by Django 2.2.5 on 2019-09-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poletopole', '0004_delete_homepagevideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomepageVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=50)),
                ('Description', models.CharField(blank=True, max_length=50)),
                ('Video_URL', models.CharField(blank=True, max_length=200)),
                ('Background_Image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
