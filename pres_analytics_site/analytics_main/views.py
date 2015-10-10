from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

def index(request):
	'''
	Index view - shows a list of all presidents to let you go to each ones dashboard.
	'''
	context = RequestContext(request)
	return render_to_response('index.html',context)
