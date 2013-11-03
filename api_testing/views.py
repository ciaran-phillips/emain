# Create your views here.


from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext, loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
import json
import calendar


def register_user(request):
	return HttpResponse("hello")
