from django.db import models

# Create your models here.


class UserProfile(models.Model):
    # imagefield also available for only images
    image = models.FileField(upload_to="images")
    # for images field we need to install extra package
    # this field validate browser as weel as Database.
    # python -m pip install Pillow
