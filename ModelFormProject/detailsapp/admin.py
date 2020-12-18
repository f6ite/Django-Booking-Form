from django.contrib import admin
from detailsapp.models import UserDetails
from detailsapp.forms import UserModelForm 
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    fields = ['BookingName', 'PubName', 'PartySize','Day', 'Time', 'TableNo', 'Email']

admin.site.register(UserDetails, BookingAdmin)
