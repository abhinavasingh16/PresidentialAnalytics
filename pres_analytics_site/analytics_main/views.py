from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
import json
import os
import copy
import sys

def index(request):
	'''
	Index view - shows a list of all presidents to let you go to each ones dashboard.
	'''
	context = RequestContext(request)
	return render_to_response('index.html',{},context)
