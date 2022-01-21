from django.db import models

# Create your models here.

#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    bio = models.CharField(max_length=256, default='')
