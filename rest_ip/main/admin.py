from django.contrib import admin
from django.utils.html import format_html

from . import models

class CIDRadmin(admin.ModelAdmin):
    list_display = ('id','address', 'status')
    search_fields = ('address',)
    list_editable = ('status',)

admin.site.register(models.CIDR, CIDRadmin)

