from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'category', 'rating', 'price', 'created_at')
	list_filter = ('category',)
	search_fields = ('name', 'email')