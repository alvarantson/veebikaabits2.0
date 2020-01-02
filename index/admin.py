from django.contrib import admin
from .models import index_text, contact, misc
# Register your models here.
admin.site.register(index_text)
admin.site.register(contact)
admin.site.register(misc)