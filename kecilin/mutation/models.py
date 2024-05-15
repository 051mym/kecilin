from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Uang_masuk(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
    nominal = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user_id}, masuk {self.nominal}"


class Uang_keluar(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
    nominal = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user_id}, keluar {self.nominal}"
