from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^api/v1/update_from_app/', 'emain_map.views.update_from_app', name='api_update_from_app'),
    url(r'^api/v1/register/', 'emain_map.views.register', name='api_register'),
)

