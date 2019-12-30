from django.shortcuts import render

# fetcheri impordid
import re
from robobrowser import RoboBrowser

def poster(request):
	return render(request, 'poster.html', context={})