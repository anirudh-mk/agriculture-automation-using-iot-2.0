import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    last_login = None
    is_active = None
    is_superuser = None
    is_staff = None
    date_joined = None

    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    phone = models.CharField(unique=True, max_length=15)
    is_active = models.BooleanField(default=False)
    profile_pic = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        if self.last_name is None:
            return self.last_name
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'user'
