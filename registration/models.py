from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    subscribed_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20, null=False)
    email = models.EmailField(blank=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ('-subscribed_date',)
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
