from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.db import models
from django.template import RequestContext, loader
from django.contrib.gis.geos import Point, Polygon
from .models import Area
import json

def index(request):
	return HttpResponse("Hello, world. You're at the areas index.")

def create(request):
	"""
	Returns the view from where the user can submit a new area.
	"""
	most_recent_area = Area.objects.order_by('-created_at').first()
	template = loader.get_template('areas/create.html')
	context = RequestContext(request, {
		'most_recent_area': most_recent_area,
	})
	return HttpResponse(template.render(context))

@csrf_exempt
def submit(request):
	"""
	Submits a new area.
	"""
	if request.method == 'POST':
		j=json.loads(request.body)
		points = j['points']
		if points:
			plist = []
			try:
				for point in points:
					plist.append(Point(float(point['lng']), float(point['lat'])))
				polygon = Polygon(plist)
			except Exception, e:
				return HttpResponseBadRequest("Wrongly drawn polygon")
			area = Area(poly=polygon)
			area.save()
			return HttpResponse(status=201)
		msg = "No points found!"
	return HttpResponseBadRequest(msg)

def check(request):
	"""
	Returns a view from where the user can check if a given spot is
	serviced from the app.
	"""
	template = loader.get_template('areas/search.html')
	return HttpResponse(template.render())

def search(request):
	"""
	Given a lat/long pair, return whether this point belongs to a serviced area.
	"""
	if request.method == 'GET':
		lat = request.GET.get('lat', None)
		lng = request.GET.get('lng', None)
		
		if lat and lng:
			point = Point(float(lng), float(lat))
			result = Area.objects.filter(poly__contains=point).exists()
			status = 200 if result else 204
			return HttpResponse(status=status)
	msg = "Bad request: not GET request or no latlong pair present"
	return HttpResponseBadRequest(msg)