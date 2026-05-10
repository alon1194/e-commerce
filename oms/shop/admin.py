from django.contrib import admin

# Register your models here.
from .models import Custumer, Address
admin.site.register(Custumer)
admin.site.register(Address)