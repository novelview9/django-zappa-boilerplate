from django.contrib import admin
from common.admin import ModelAdmin
from .models import Order


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    pass


