# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
import datetime

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'message' : 'This is where our map will be'
	})
	return HttpResponse(template.render(context))

# TODO add POST for ping from the app
def update_from_app(request):

    # everything ok
    return HttpResponse(status=200)

# TODO display current status on the map
