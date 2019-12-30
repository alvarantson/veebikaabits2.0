import datetime
import math
# fetcheri impordid
import re
from robobrowser import RoboBrowser
from .fetcher import okidoki_fetch, osta_fetch, kuldnebors_fetch, soov_fetch, täpitähed
from .models import report,browser_text,blacklist,search_history

def searcher(search_item, okidoki_check, soov_check, osta_check, kuldnebors_check, min_price, max_price, filters):
	timer = datetime.datetime.now().strftime('%M:%S.%f')[:-4]
#		ITEM = [ #counter, URL, NAME, IMG_URL, [ AUCTION_PRICE, BUY_NOW_PRICE ], SHOP ]
#	OKIDOKI
	items = []
#			if str(request.POST.get('okidoki')) == 'on':
	if okidoki_check == 'on':
		try:
			okidoki_counter = len(items)
			items += okidoki_fetch(search_item)
			okidoki_counter -= len(items)
			okidoki = '1'
		except:
			okidoki = '0'
			okidoki_counter = 0
			report.objects.create(
				app_name='okidoki',
				search_item=search_item,
				date_time=datetime.datetime.now(),
				misc='browser search'
				)
	else:
		okidoki = '0'
		okidoki_counter = 0
#	SOOV
#			if str(request.POST.get('soov')) == 'on':
	if soov_check == 'on':
		try:
			soov_counter = len(items)
			items += soov_fetch(search_item)
			soov_counter -= len(items)
			soov = '1'
		except:
			soov = '0'
			soov_counter = 0
			report.objects.create(
				app_name='soov',
				search_item=search_item,
				date_time=datetime.datetime.now(),
				misc='browser search'
				)
	else:
		soov = '0'
		soov_counter = 0
#	OSTA
#			if str(request.POST.get('osta')) == 'on':
	if osta_check == 'on':
		try:
			osta_counter = len(items)
			items += osta_fetch(search_item)
			osta_counter -= len(items)
			osta = '1'
		except:
			osta = '0'
			osta_counter = 0
			report.objects.create(
				app_name='osta',
				search_item=search_item,
				date_time=datetime.datetime.now(),
				misc='browser search'
				)
	else:
		osta = '0'
		osta_counter = 0
#	KULDNEBORS
#			if str(request.POST.get('kuldnebors')) == 'on':
	if kuldnebors_check == 'on':
		try:
			kuldnebors_counter = len(items)
			items += kuldnebors_fetch(search_item)
			kuldnebors_counter -= len(items)
			kuldnebors = '1'
		except:
			kuldnebors = '0'
			kuldnebors_counter = 0
			report.objects.create(
				app_name='kuldnebors',
				search_item=search_item,
				date_time=datetime.datetime.now(),
				misc='browser search'
				)
	else:
		kuldnebors = '0'
		kuldnebors_counter = 0
	
	search_history.objects.create(
		search_item=search_item,
		time_elapsed = math.fabs(round((float(timer.split(':')[1])+float(timer.split(':')[0])*60)-(float(datetime.datetime.now().strftime('%M:%S.%f')[:-4].split(':')[1])+float(datetime.datetime.now().strftime('%M:%S.%f')[:-4].split(':')[0])*60),3)),
		search_datetime= datetime.datetime.now().strftime('%b %d %Y %I:%M%p'),
		items_total=str(len(items)),
		items_okidoki=str(math.fabs(okidoki_counter)),
		items_osta=str(math.fabs(osta_counter)),
		items_soov=str(math.fabs(soov_counter)),
		items_kuldnebors=str(math.fabs(kuldnebors_counter))
	)
	return items


def filterer(items, okidoki_check, soov_check, osta_check, kuldnebors_check, min_price, max_price, filters):
	items_final = []
	for i in items:
		if min_price != '0':
			i[4][0] = i[4][0].replace(' ','')
			i[4][1] = i[4][1].replace(' ','')
			if i[4][0] == '-' and i[4][1] == '-':
				pass
			if i[4][1] != '-':
				if float(i[4][1]) >= float(min_price) and float(i[4][1]) <= float(max_price):
					items_final.append(i)
				else:
					pass
			if i[4][0] != '-':
				if float(i[4][0]) >= float(min_price) and float(i[4][0]) <= float(max_price):
					items_final.append(i)
				else:
					pass
		else:
			if i[4][0] != '-':
				if float(i[4][0]) <= float(max_price):
					items_final.append(i)
			if i[4][1] != '-':
				if float(i[4][1]) <= float(max_price):
					items_final.append(i)
			if i[4][0] == '-' and i[4][1] == '-':
				items_final.append(i)

	for item in items_final:
		if items_final.count(item) != 1:
			for i in range(1,items_final.count(item)):
				items_final.remove(item)

	items_final2 = []

	if filters != 'no-filter':
		for item in items_final:
			if item[4][1] != '-':
				items_final2.append(item)
	else:
		items_final2 = items_final



	if filters == 'l-2-h':
		items_final2.sort(key=lambda x: float(x[4][1]))

	if filters == 'h-2-l':
		items_final2.sort(key=lambda x: float(x[4][1]), reverse=True)

	if filters == 'a-2-z':
		items_final2.sort(key=lambda x: x[2])

	if filters == 'z-2-a':
		items_final2.sort(key=lambda x: x[2], reverse=True)

	try:
		items_final = items_final2
	except:
		pass

	

	return items_final