from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^registration/', 'api_testing.views.register_user', name='register_user_test')
)

