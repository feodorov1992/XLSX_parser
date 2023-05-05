from django.contrib import admin
from django.contrib.admin import TabularInline

from core.models import UploadedFile, StatDataItem


class StatDataItemInline(TabularInline):
    model = StatDataItem
    extra = 0
    can_delete = False
    max_num = 0
    readonly_fields = ('id', 'date', 'company',
                       'fact_qliq_data1', 'fact_qliq_data2', 'fact_qoil_data1', 'fact_qoil_data2',
                       'forecast_qliq_data1', 'forecast_qliq_data2', 'forecast_qoil_data1', 'forecast_qoil_data2',)


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    inlines = [StatDataItemInline]
