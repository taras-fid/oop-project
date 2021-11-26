from django.contrib import admin
from .models import Requisite, RequisiteHistory, RequisiteType, RequisitePosterRole

admin.site.register(Requisite)
admin.site.register(RequisiteHistory)
admin.site.register(RequisiteType)
admin.site.register(RequisitePosterRole)
