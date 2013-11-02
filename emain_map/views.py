# Create your views here.

from django.http import HttpResponse
import datetime

def index(request):
	return HttpResponse("This is our map")


# TODO add POST for ping from the app
# TODO display current status on the map
