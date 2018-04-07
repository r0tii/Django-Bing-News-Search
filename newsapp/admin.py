from django.contrib import admin

# Register your models here.
from .models import SearchTerm

class SearchAdmin(admin.ModelAdmin):
    list_display = ('term', 'time',)
    list_filter = ('time',)
    search_fields = ('term',)
    date_hierarchy = 'time'

    list_per_page = 25

admin.site.register(SearchTerm, SearchAdmin)