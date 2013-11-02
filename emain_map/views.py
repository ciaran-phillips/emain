# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
import datetime
import json
import calendar
from models import Location, Project, Message
from django.contrib.auth.models import User



def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'message' : 'This is where our map will be'
	})
	return HttpResponse(template.render(context))

def map_data(request):
	# Dummy value for now
	current_project = 1
	response_data = {}
	response_data['users'] = []
	users = User.objects.filter(participating_in=current_project)

	for u in users:
		user_dict = {}
		user_dict['first_name'] = u.first_name
		user_dict['last_name'] = u.last_name
		user_dict['locations'] = []
		user_locations = u.location_set.all()
		for loc in user_locations:
			user_loc = {}
			user_loc['lat'] = loc.lat
			user_loc['lon'] = loc.lon
			user_loc['time'] = calendar.timegm(loc.when.utctimetuple())
			user_dict['locations'].append(user_loc)
		response_data['users'].append(user_dict)
	return HttpResponse(json.dumps(response_data), content_type="application/json")
	
# TODO add POST for ping from the app
def update_from_app(request):

    # everything ok
    return HttpResponse(status=200)

# TODO display current status on the map
