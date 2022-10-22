from traceback import format_list
from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality' : 100},
    )