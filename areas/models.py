from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

from django.contrib.gis.db import models

class Area(models.Model):

	created_at = models.DateTimeField(editable=False)

	# GeoDjango-specific: a geometry field (PolygonField)
	poly = models.PolygonField()
	objects = models.GeoManager()

	def save(self, *args, **kwargs):
		'''On save add timestamp'''
		if not self.id:
			self.created_at = timezone.now()
		return super(Area, self).save(*args, **kwargs)