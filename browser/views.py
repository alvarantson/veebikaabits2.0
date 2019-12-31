from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
import math
# fetcheri impordid
import re
from robobrowser import RoboBrowser
from .fetcher import okidoki_fetch, osta_fetch, kuldnebors_fetch, soov_fetch, täpitähed
from .models import report,browser_text,blacklist,search_history
from .searcher import searcher, filterer

def browser(request):

	


	MINIMUM_LETTER_COUNT = 2
	MAXIMUM_LETTER_COUNT = 999

	blacklisted = blacklist.objects.all()[0].words
	try:
		search_item = request.session['search']
		del request.session['search']
		if search_item in blacklisted.split(';') or len(search_item) <= MINIMUM_LETTER_COUNT or len(search_item) > MAXIMUM_LETTER_COUNT:
			return HttpResponse('<h4><a href="/browser">Tagasi otsingusse. </a>Te ei: \nkasutanud vahemalt '+str(MINIMUM_LETTER_COUNT+1)+' tähemärki \nkasutasite üle '+str(MAXIMUM_LETTER_COUNT)+' tähemärgi \nvõi kasutasite mõnda neist keelatud otsingutest: \n\n'+blacklisted.replace(';',', \n')+'</h4>')
		
#		def searcher(search_item, okidoki_check, soov_check, osta_check, kuldnebors_check, min_price, max_price, filters):
		items = searcher(
			search_item,
			'on',
			'on',
			'on',
			'on',
			'0',
			'10000',
			'no-filter'
			)

		request.session['storage'] = [search_item,items,'on','on','on','on','0','10000','no-filter']
		return render(request, 'browser.html', context={'lang': browser_text.objects.all()[0],'filter': 'no-filter','itemname': search_item,'items':items, 'min_price': '0', 'max_price': '10000',  'okidoki': 'on', 'osta': 'on', 'soov': 'on', 'kuldnebors': 'on'})
	except:
		pass

	if bool(request.POST) == True:
		if request.POST['submit-btn'] == 'search-item':
			timer = datetime.datetime.now().strftime('%M:%S.%f')[:-4]

			print(request.POST['item-name'])
			if request.POST['item-name'] in blacklisted.split(';') or len(request.POST['item-name']) <= MINIMUM_LETTER_COUNT or len(request.POST['item-name']) > MAXIMUM_LETTER_COUNT:
				return HttpResponse('<h4><a href="/browser">Tagasi otsingusse. </a>Te ei: \nkasutanud vahemalt '+str(MINIMUM_LETTER_COUNT+1)+' tähemärki \nkasutasite üle '+str(MAXIMUM_LETTER_COUNT)+' tähemärgi \nvõi kasutasite mõnda neist keelatud otsingutest: \n\n'+blacklisted.replace(';',', \n')+'</h4>')

#		def searcher(search_item, okidoki_check, soov_check, osta_check, kuldnebors_check, min_price, max_price, filters):

			try: # IF ITEM SEARCH NAME DOESNT CHANGE
				if request.POST['item-name'] == request.session['storage'][0]:
					items = searcher(
					search_item,
					'on',
					'on',
					'on',
					'on',
					'0',
					'10000',
					'no-filter'
					)
#					items = filterer(
#						items,
#						str(request.POST.get('okidoki')),
#						str(request.POST.get('soov')),
#						str(request.POST.get('osta')),
#						str(request.POST.get('kuldnebors')),
#						request.POST['min-price'],
#						request.POST['max-price'],
#						request.POST['filter']
#						)
					return render(request, 'browser.html', context={'lang': browser_text.objects.all()[0],'filter': 'no-filter','itemname': '','items':items, 'min_price': '0', 'max_price': '10000', 'okidoki': 'on', 'osta': 'on', 'soov': 'on', 'kuldnebors': 'on'})
			except:
				pass

			items = searcher(
				request.POST['item-name'],
				"on",
				"on",
				"on",
				"on",
				"0",
				"10000",
				"no-filter"
				)

			request.session['storage'] = [request.POST['item-name'],items,str(request.POST.get('okidoki')),str(request.POST.get('soov')),str(request.POST.get('osta')),str(request.POST.get('kuldnebors')),"0","10000","no-filter"]


			return render(request, 'browser.html', context={'lang': browser_text.objects.all()[0],'filter': 'no-filter','itemname': '','items':items, 'min_price': '0', 'max_price': '10000', 'okidoki': 'on', 'osta': 'on', 'soov': 'on', 'kuldnebors': 'on'})
	return render(request, 'browser.html', context={'lang': browser_text.objects.all()[0],'filter': 'no-filter','itemname': '','items':[], 'min_price': '0', 'max_price': '10000', 'okidoki': 'on', 'osta': 'on', 'soov': 'on', 'kuldnebors': 'on'})