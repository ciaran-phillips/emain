# Create your views here.

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext, loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
import json
import calendar
from models import Location, Project, Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import Location
from .forms import LocationForm

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, { 'message' : 'This is where our map will be' })
    return HttpResponse(template.render(context))

def map_data(request, userid = None):
	# Dummy value for now
	
	current_project = 1
	response_data = {}
	response_data['users'] = []
	if not userid:
		users = User.objects.filter(participating_in=current_project)
	else:
		userid = int(userid)
		users = User.objects.filter(pk = userid)
	#assert False, locals()
	for u in users:
		user_dict = {}
		user_dict['id'] = u.pk
		user_dict['first_name'] = u.first_name
		user_dict['last_name'] = u.last_name
		user_dict['locations'] = []
		user_locations = u.location_set.all()
		for loc in user_locations:
			user_loc = {}
			user_loc['lat'] = loc.lat
			user_loc['lon'] = loc.lon
			t = loc.when.strftime("%H:%M:%S")
			user_loc['time'] = t
			user_dict['locations'].append(user_loc)
			
		response_data['users'].append(user_dict)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

# TODO add POST for ping from the app
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

def register(request):
    # TODO proper form
    un = request.POST['username']
    pw = request.POST['password']
    user = User.objects.create_user(username=un, password=pw)
    user.save()
    user = authenticate(username=un, password=pw)
    login(request, user)
    return HttpResponse(content=str(user.id), status=200)
