from newsfeed.models import StreamItem
from django.shortcuts import render_to_response
from user_utility import *

def homepage(request):


    context = {
        'stream_item_list': StreamItem.objects.all().order_by('-date_added')[:10],
    }

    return render_to_response('newsfeed/newsfeed.html', context)
