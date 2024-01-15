from django.contrib import admin
from card.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_number', 'uuid')
