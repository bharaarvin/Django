from re import search
from django.contrib import admin
from . models import Guest

# Register your models here.

class TampilGuest(admin.ModelAdmin):
    list_display = ('nim', 'nama', 'kegiatan')
    list_display_links = (None)
    search_fields = ('nim', 'nama')

admin.site.register(Guest, TampilGuest)