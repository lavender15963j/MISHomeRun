from django.contrib import admin

from models import *

admin.site.register(Team)

class StatAdmin(admin.ModelAdmin):
    list_display = ('name','year')


admin.site.register(Stat, StatAdmin)
