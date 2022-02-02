from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=300)

    def __str__(self):
        return str(self.user)


class ImageVerifaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    vrified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
