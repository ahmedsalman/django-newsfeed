from django.db.models import signals
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from iTest.base.models import TimeStampAwareModel
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from aceprofile.models import AceProfile


class StreamItem(TimeStampAwareModel):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    actor = models.ForeignKey( User, null = True, blank = True )
    actor_profile = models.ForeignKey( AceProfile, null = True, blank = True )


    def get_rendered_html(self):
        template_name = 'newsfeed/%s.html' % (self.content_type.name)
        return render_to_string(template_name, { 'object': self.content_object })


#def update_item(instance, raw, created, **kwargs):
#    if created:
#        item = StreamItem()
#        item.content_type = ContentType.objects.get_for_model(type(instance))
#        item.object_id = instance.id
#        item.actor = instance.created_by
#        try:
#            item.actor_profile = AceProfile.objects.get( profile_owner = instance.created_by )
#        except AceProfile.DoesNotExist:
#            pass
#        item.save()


#signals.post_save.connect(update_item, MyModel)
