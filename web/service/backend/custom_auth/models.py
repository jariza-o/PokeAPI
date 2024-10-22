from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class Custom_User(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Hash the password before saving the user
        self.password = make_password(self.password)
        super(Custom_User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email