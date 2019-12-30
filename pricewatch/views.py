from django.shortcuts import render

# Create your views here.
def pricewatch(request):
	return render(request, 'pricewatch.html', context={})