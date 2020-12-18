from django.shortcuts import render
from django.db import models
from detailsapp.models import UserDetails
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from unicodedata import normalize

# Create your views here.

from .forms import UserModelForm

# add to your views
def userDetails(request):
    form = UserModelForm()
    args = {}
    if request.method == 'POST':
        form = UserModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            users = UserDetails.objects.all()

            return render(request, 'display0.html', {'users': users})


    else:
        form_class = UserModelForm
    args['form'] = form

    return render(request, 'userdetails.html', args)
