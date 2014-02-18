Django Newsfeed Documentation
===================================

`django newsfeed' is a facebook alike newsfeed app for Django

Newsfeeds are actually actions events

For example: `justquick <https://github.com/justquick/>`_ ``(actor)`` *closed* ``(content_object)`` 12 hours ago

Installation
============

Installation is easy using ``pip`` and will install all required libraries.

::
get it from source

::

    $ git clone https://github.com/brantyoung/django-newsfeed


Then to add the Django Newsfeed to your project add the app ``newsfeed`` to your ``INSTALLED_APPS`` and urlconf.

The app should go somewhere after all the apps that are going to be generating newsfeed like ``django.contrib.auth``::

    INSTALLED_APPS = (
        'django.contrib.auth',
        ...
        'newsfeed',
        ...
    )

Add the newsfeed urls to your urlconf::
    
    import newsfeed
    
    urlpatterns = patterns('',
        ...
        ('^inbox/newsfeed/', include(newsfeed.urls)),
        ...
    )


Generating newsfeed
=========================

Generating newsfeed is probably best done in a separate signal.

::

    from django.db.models.signals import post_save
    from newsfeed import notify
    from myapp.models import MyModel

    def update_item(instance, raw, created, **kwargs):
        if created:
            item = StreamItem()
            item.content_type = ContentType.objects.get_for_model(type(instance))
            item.object_id = instance.id
            item.actor = instance.created_by
            item.save()

    signals.post_save.connect(update_item, MyModel)



Model methods
-------------

``obj.get_rendered_html``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This methon generate newsfeed for that instant


Create Tamplate for each model name for which you want to generate newsfeed
------------------------------------------------------------------------------


::

<div class="row post-entry">
	<div class="span1">
		<div class="post-userphoto">
		    <a href="#" title="View users profile">
		    <img src="/static/img/generic/photo.png" style="height:48px; width:48px;" class="member-photo"></a>
		</div>
	</div>

	<div class="span9">
		<div class="post-text">
			<div class="post-title">
			    <a href="{% url user_profile_home object.created_by.id %}"><h2>{{ object.created_by }} downloaded fileds of {{ object.ip.name }} IP</h2></a>
            </div>
            {{object.ip.description}}
        </div>

		<div class="newsfeedpcb-template">
			<div class="pcb-container">
                    <a href="{% url ip_description object.ip.id %}"><img src="/static/img/generic/chip.png" width="100" height="75" /></a>
				<div class="" >
					<ul class="">
                        <a href="{% url file_download  object.ip.id %}" name="download"> Download files</a>
					</ul>
				</div>
			</div>
		</div>

       <div class="ipRows">

            <div class="ipDescription">
            <div class="caption"><strong>Name:</strong></div>
            <div class="details"><a style="color:black" href="{% url ip_description object.ip.id %}">{{ object.ip.name }}</a></div> 
            </div>
            <br />

            <div class="ipDescription">
            <div class="caption"><strong>BU:</strong></div>
            <div class="details">{% if object.ip.bu %} {{ object.ip.get_bu_display }} {% else %} Not Defined {% endif %}</div> 
            </div>             
            <br />

            <div class="ipDescription">
            <div class="caption"><strong>LOB:</strong></div>
            <div class="details">{% if object.ip.lob %} {{ object.ip.get_lob_display }}  {% else %} Not Defined {% endif %} </div> 
            </div>             
            <br />

            <div class="ipDescription">
            <div class="caption"><strong>Process Node:</strong></div>
            <div class="details">{% if object.ip.process_node %} {{ object.ip.process_node }}  {% else %} Not Defined {% endif %}</div> 
            </div>             

        </div>
    </div>
</div>


