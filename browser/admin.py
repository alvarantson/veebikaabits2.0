from django.contrib import admin
from .models import report, browser_text, blacklist, search_history
# Register your models here.
admin.site.register(report)
admin.site.register(browser_text)
admin.site.register(blacklist)
admin.site.register(search_history)