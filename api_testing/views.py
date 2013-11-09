# Create your views here.


from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext, loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
import json
import calendar
from emain_map import forms

def register_user(request):
    form = forms.RegistrationForm()
    context = RequestContext(request, {
        'form' : form
    })
    template = loader.get_template('api_testing/registration.html')
    return HttpResponse(template.render(context))
