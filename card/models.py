import uuid

from django.db import models


class Card(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=255, blank=False, null=False)
    contact_number = models.CharField(max_length=255, blank=False, null=False)
    mc_dot_number = models.CharField(max_length=255, blank=False, null=False)
    number_of_trucks = models.IntegerField(blank=False, null=False)
    fuel_cards_register = models.CharField(max_length=255, blank=False, null=False)
    mailing_address = models.CharField(max_length=255, blank=False, null=False)
    address_line = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(max_length=255, blank=False, null=False)
    zip_code = models.CharField(max_length=255, blank=False, null=False)
    primary_contact_info = models.CharField(max_length=255, blank=False, null=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=255, blank=False, null=False)
    email_address = models.EmailField(max_length=255, blank=False, null=False)
    file = models.FileField(upload_to='files/', blank=False, null=False)
    signature = models.ImageField(upload_to='signature/', blank=False, null=False)

    def __str__(self):
        return self.company_name
