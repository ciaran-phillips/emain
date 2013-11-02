# Create your views here.

from django.http import HttpResponse
import datetime

def index(request):
	return HttpResponse("This is our map")
