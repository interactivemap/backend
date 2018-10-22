from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Territory, PoliticalEntity, DiplomaticRelation

# Register your models here.
admin.site.register(Territory, SimpleHistoryAdmin)
admin.site.register(PoliticalEntity, SimpleHistoryAdmin)
admin.site.register(DiplomaticRelation, SimpleHistoryAdmin)
