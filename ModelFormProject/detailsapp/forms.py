from django.forms import ModelForm
from detailsapp.models import UserDetails
from django import forms
from unicodedata import normalize
from django.core.exceptions import ValidationError

class UserModelForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['BookingName', 'PubName', 'PartySize','Day', 'Time', 'TableNo', 'Email']

    def clean_BookingName(self): 
        BookingName = self.cleaned_data.get('BookingName')
        PubName = self.cleaned_data.get('PubName')

        if (BookingName == ""):
            raise ValidationError('The Booking Name field cannot be left blank.')
            
        for instance in UserDetails.objects.all():
            if instance.PubName == PubName:
                if instance.BookingName == BookingName:
                        raise ValidationError(BookingName + ' already has a booking.')
        return BookingName

    def clean_TableNo(self):
        PubName = self.cleaned_data.get('PubName')
        TableNo = self.cleaned_data.get('TableNo')
        Day = self.cleaned_data.get('Day')
        Time = self.cleaned_data.get('Time')
      
        if (Day == ""):
            raise ValidationError("Please select a day.")

        if (Time == ""):
            raise ValidationError("Please select a timeslot.")
        
        if (PubName == ""):
            raise ValidationError("Please select a pub.")
        
        if (TableNo == ""):
            raise ValidationError("Please select a table.")


        for instance in UserDetails.objects.all():
            if instance.PubName == PubName:
                if instance.TableNo == TableNo:
                    if instance.Day == Day:
                        if instance.Time == Time:
                            raise ValidationError('This table is already booked at that time, please change table number or try another time.')
        return TableNo
        

        
        
    