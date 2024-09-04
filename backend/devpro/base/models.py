from django.db import models
from django_min_custom_user.models import MinAbstractUser


class User(MinAbstractUser):
    pass


class Arquivo(models.Model):
    arq = models.FileField(upload_to='public/')
    privado = models.FileField(upload_to='private/')
