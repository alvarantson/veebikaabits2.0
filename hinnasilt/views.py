from django.shortcuts import render

# Create your views here.
def hinnasilt(request):
	return render(request, 'hinnasilt.html', context={})