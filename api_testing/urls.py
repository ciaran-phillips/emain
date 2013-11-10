from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^registration/', 'api_testing.views.register_user', name='register_user_test'),
    url(r'^user_map/', 'api_testing.views.user_map', name='user_map'),
)

