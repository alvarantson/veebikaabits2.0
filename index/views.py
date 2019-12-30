from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import index_text, contact
# Create your views here.
def index(request):
	if bool(request.POST) == True:
		request.session['search'] = request.POST['search']
		return HttpResponseRedirect('/browser')
	return render(request, 'index.html', context={'lang':index_text.objects.all()[0], 'contact':contact.objects.all()[0]})