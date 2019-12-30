# YouTube Video: https://www.youtube.com/watch?v=hrdDIrT9kJI
def täpitähed(sõne):
	sõne = sõne.replace('&#228;','ä')
	sõne = sõne.replace('&#245;','õ')
	sõne = sõne.replace('&#220;','ü')
	return sõne

#	OKIDOKI.ee
#	CAPS LOCKis on koik, mida on vaja final listi appendiks vaja, ehk otsitavad muutujad.

def okidoki_fetch(OTSING):
	import re
	from robobrowser import RoboBrowser
	browser = RoboBrowser()
	browser.open("https://www.okidoki.ee/buy/all/?p=1&query="+OTSING+"&c=0")



	try:
		lk_nr = str(browser.select("#current-page"))
		page_numbers = str(lk_nr.encode('utf-8')).split('b>')[1]
		page_numbers = page_numbers.split('\\xc2\\xa0/\\xc2\\xa0')
		page_numbers = [int(page_numbers[0]),int(page_numbers[1].replace('</',''))]
	except:
		all_items = []
		return all_items

	all_items = []
	for page_number in range(page_numbers[0],page_numbers[1]+1):
		browser.open("https://www.okidoki.ee/buy/all/?p="+str(page_number)+"&query="+OTSING+"&c=0")
		items = browser.select('.classified-content')
		counter = 0
		for item in items:
			counter += 1
			URL = 'https://www.okidoki.ee'+str(item).split('"')[5]
			NAME = (str(item).split('<h3')[1].split('</a>')[0].split('">')[1])
			IMG_URL = str(item).split('"')[13]
			try:
				PRICE = str(item).split('"')[str(item).split('"').index('price')+1].replace('><b>','').split(' &#8364')[0]
			except:
				PRICE = '-'
			if 'M&#228;&#228;ramata</b>' in PRICE:
				PRICE = '-'
			if ' ' in PRICE:
				PRICE = PRICE.replace(' ','')
			if '€</b><smallclass=' in PRICE:
				PRICE.replace('€</b><smallclass=','')
			PRICE = PRICE.split('€')[0]
			if '<b>' in PRICE:
				PRICE = PRICE.split('<b>')[1]
			if 'Määramata' in PRICE:
				PRICE = '-'
			try:
				PRICE = str(int(PRICE))
			except:
				PRICE = '-'
			PRICE = ['-',PRICE]
			all_items.append(['#'+str(counter),URL,NAME,IMG_URL,PRICE,'OKIDOKI'])
	return all_items


# 	OSTA.ee

def osta_fetch(OTSING):
	import re
	from robobrowser import RoboBrowser
	browser = RoboBrowser()
	browser.open('https://osta-ee.postimees.ee/index.php?fuseaction=search.search&id=1000&q%5Bq%5D='+OTSING+'&q%5Bshow_items%5D=1&q%5Bshow_shop%5D=1&q%5Bcat%5D=1000&q%5Bfuseaction%5D=search.search&start=1&pagesize=180')

	try:
		page_numbers = int(str(browser.select(".totalPageCount")).replace('</span>]','').split('Count">')[1])
	except:
		all_items = []
		return all_items

	all_items = []
	for page_number in range(0,page_numbers):
		browser.open('https://osta-ee.postimees.ee/index.php?fuseaction=search.search&id=1000&q%5Bq%5D='+OTSING+'&q%5Bshow_items%5D=1&q%5Bshow_shop%5D=1&q%5Bcat%5D=1000&q%5Bfuseaction%5D=search.search&start='+str(page_number*18)+'1&pagesize=180')
		items = browser.select('.col-md-4')
		counter = 0
		for item in items:
			counter += 1
			try:
				NAME = str(item.select('.offer-thumb__title')).split('"')[3]
			except:
				continue
			IMG_URL = str(item.select('.offer-thumb__image')).split('"')[13]
			URL = 'https://osta-ee.postimees.ee/'+str(item.select('.offer-thumb__image')).split('"')[17]
			if '.html' not in URL:
				continue
			PRICE = [] # 1. on hetke hind 2. on osta kohe hind
			try:
				PRICE.append(str(item.select('.price-cp')).replace('</span>','').split('>')[1].replace('€]',''))
			except:
				PRICE.append('-')
			try:
				PRICE.append(str(item.select('.price-bn')).replace('</span>','').split('>')[1].replace('€]',''))
			except:
				PRICE.append('-')
			PRICE[0] = PRICE[0].replace(' ','')
			PRICE[1] = PRICE[1].replace(' ','')
			all_items.append(['#'+str(counter),URL,NAME,IMG_URL,PRICE,'OSTA'])

	return all_items

def kuldnebors_fetch(OTSING):
	import re
	from robobrowser import RoboBrowser
	browser = RoboBrowser()
	browser.open('https://www.kuldnebors.ee/search/search.mec?pob_evt=onpageindex&pob_action=search&pob_page_index=1&pob_page_size=100&search_evt=onsearch&search_O_string='+OTSING+'&pob_evt_param=1')



	try:
		page_numbers = int(str(browser.select("#pob_page_index")[0].parent).split('"/> / ')[1].replace('\\xa0\\xa0</td>','').replace('</td>',''))
	except:
		all_items = []
		return all_items

	

	all_items = []
	for page_number in range(0,page_numbers+1):
		browser.open('https://www.kuldnebors.ee/search/search.mec?pob_evt=onpageindex&pob_action=search&pob_page_index=1&pob_page_size=100&search_evt=onsearch&search_O_string='+OTSING+'&pob_evt_param='+str(page_number*10)+'1')
		items = browser.select('.post-row')
		counter = 0
		all_items1 = []

#	CANCERBORSis on igat itemit kahes samaclassiga divis, sp kaks step2 loopi, kuna yhes on pool infot ja teises ylejaanud
		for item in items[::2]:
			counter += 1
			try:
				IMG_URL = str(item.select('img')[0]).split('src="')[1].split('" title="')[0]
			except:
				IMG_URL = '-'
			if 'margin' in IMG_URL:
				IMG_URL = IMG_URL.split('" style')[0]
			if 'title' in IMG_URL:
				IMG_URL = IMG_URL.split('" title')[0]

			PRICE = str(item.select('b')[0]).replace('<b>','')
			if PRICE == '</b>':
				PRICE = '-'
				PRICE = ['-',PRICE]
			else:
				PRICE = PRICE.replace(' €</b>','')
				if ',' in PRICE:
					PRICE = PRICE.replace(',','.') # CANCERBORS sucks ass - nad on asendanud floatidel punktid komadega
				if len(PRICE) > 3 and len(PRICE) < 10: # CANCERBORS paneb tuhandetele vahed vahele, nt 10 000
					PRICE = PRICE.replace(' ','')
				try:
					PRICE = str(float(PRICE))
					PRICE = ['-',PRICE]
				except:
					PRICE = PRICE.split('fg7">')[1].split('€</span>')[0]
					if len(PRICE) > 3 and len(PRICE) < 10: # CANCERBORS paneb tuhandetele vahed vahele, nt 10 000
						PRICE = PRICE.replace(' ','')
					PRICE = ['-',PRICE]
				
			all_items1.append([counter,IMG_URL,PRICE])
		
		counter = 0
		all_items2 = []
		for item in items[1::2]:
			counter += 1
			URL = 'https://www.kuldnebors.ee/'+str(item).split('data-post-row="')[1].split('">')[0]
			NAME = str(item.select('span')[0]).split('">')[1].split('</span')[0]
			all_items2.append([counter,URL,NAME])

		for i in all_items1:
			all_items.append(['#'+str(i[0]), all_items2[i[0]-1][1], all_items2[i[0]-1][2], i[1], i[2], 'KULDNEBORS'])
	return all_items


def soov_fetch(OTSING):
	import re
	from robobrowser import RoboBrowser
	browser = RoboBrowser()
	browser.open('https://soov-ee.postimees.ee/keyword-'+OTSING+'/listings.html')

	try:
		page_numbers = int(str(browser.select('.pagination')[0].select('li')[len(browser.select('.pagination')[0].select('li'))-2]).split('.html">')[1].split('</a')[0])
	except:
		all_items = []
		return all_items

	all_items = []
	for page_number in range(1,page_numbers+1):
		browser.open("https://soov-ee.postimees.ee/keyword-"+OTSING+"/"+str(page_number)+"/listings.html")
		items = browser.select('.item-list')
		counter = 0
		for item in items[2:]: # esimesed kaks on listingute kohal need salvesta otsing ja selles nimekirjas on ka 0 kuulutust valismaalt error disclaimer, kuna need on sama class nameiga
			if 'Soovin' in str(item.select('span.thin')):
				pass
			if 'Müüa' in str(item.select('span.thin')):
				counter += 1
				NAME = str(item.select('img')).replace('[<img alt="','').split('" class')[0]
				if 'alt="' in NAME:
					NAME = NAME.split('alt="')[1]
				IMG_URL = str(item.select('img')).replace('"/>]','').split('src="')[1].split('"/>')[0]
				try:
					PRICE = str(item.select('.item-price')).split('margin">')[1].split('€<')[0]
					PRICE = ['-',PRICE]
				except:
					PRICE = '-'
					PRICE = ['-',PRICE]
				URL = str(item.select('.add-title')[0].select('a')).split('ref="')[1].split('">')[0]
				all_items.append(['#'+str(counter),URL,NAME,IMG_URL,PRICE,'SOOV'])
	return all_items