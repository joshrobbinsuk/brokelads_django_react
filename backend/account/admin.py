from django.contrib import admin

from .models import CustomerUser
from bookmaker.models import TransactionRecord


@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    pass
