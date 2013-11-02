# Create your views here.

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext, loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime

from .models import Location
from .forms import LocationForm

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'message' : 'This is where our map will be'
	})
	return HttpResponse(template.render(context))

# login required
def update_from_app(request):
    if request.method == 'GET':
        return HttpResponseBadRequest()
    form = LocationForm(request.POST)
    if not form.is_valid():
        print form.errors
        return HttpResponseBadRequest()
    else:
        location = form.save(commit=False)
        location.user = request.user
        location.save()
        # everything ok
        return HttpResponse(status=200)

# TODO display current status on the map
