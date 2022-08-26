from django.contrib import admin
from . models import Post, Kategoti
# Register your models here.

class TampilBuku(admin.ModelAdmin):
    list_display = ('judul', 'kategori')
    list_display_links = (None)
    search_fields = ('judul', 'kategori')

admin.site.register(Post, TampilBuku)
admin.site.register(Kategoti) 