from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class User(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     password = models.CharField(max_length=64)
#     secret = models.CharField(max_length=128)
#     def __str__(self):
#         return self.first_name + " " + self.last_name


class TimeLog(models.Model):
    user = models.ForeignKey(User, related_name="timelog_user")
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField(null=True)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name()


class NfcCard(models.Model):
    user = models.ForeignKey(User, related_name="nfccard_user")
    card_name = models.CharField(max_length=64)
    serial_number = models.CharField(max_length=64)
    secret_key = models.CharField(max_length=64)

# i am a comment
