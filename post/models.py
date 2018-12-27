from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete='None')
    title = models.CharField(max_length=50)
    content = RichTextField()
    image = models.ImageField(upload_to='post_images/', default='post_images/default_image.png')
    date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
