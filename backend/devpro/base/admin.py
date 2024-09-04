from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django_min_custom_user.admin import MinUserAdmin

from devpro.base.models import User, Arquivo


@admin.register(User)
class UserAdmin(MinUserAdmin):
    pass


@admin.register(Arquivo)
class ArquivoAdmin(ModelAdmin):
    pass
