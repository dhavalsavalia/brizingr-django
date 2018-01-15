from django.contrib import admin

from .models import BillingProfile, Charge

admin.site.register(BillingProfile)
admin.site.register(Charge)