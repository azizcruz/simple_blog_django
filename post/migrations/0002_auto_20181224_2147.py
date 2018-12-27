# Generated by Django 2.2.dev20181222235254 on 2018-12-24 21:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post_images/default_image.png', upload_to='post_images/'),
        ),
    ]