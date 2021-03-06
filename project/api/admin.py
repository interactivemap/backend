from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *
from .forms import TerritoryForm


# Register your models here.
@admin.register(Territory)
class TerritoryAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    form = TerritoryForm
    include = "__all__"


admin.site.register(PoliticalEntity, SimpleHistoryAdmin)
admin.site.register(DiplomaticRelation, SimpleHistoryAdmin)

admin.site.site_header = "ChronoScio Database"
admin.site.site_title = "ChronoScio editor"
admin.site.index_title = "Edit data"
