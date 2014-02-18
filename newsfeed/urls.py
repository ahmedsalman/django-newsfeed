from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

from newsfeed.views import *

urlpatterns = patterns('',
    url(r'^$', homepage, name = 'homepage'),
)

