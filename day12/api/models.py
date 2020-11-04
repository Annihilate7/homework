from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 't_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Computer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.CharField(max_length=20, verbose_name='厂商')

    class Meta:
        db_table = 't_computer'
        verbose_name = '笔记本电脑'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
