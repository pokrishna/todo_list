from django.contrib import admin
from todo_app.models import todo_list
import csv
from django.http import HttpResponse
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected"
class todo_listAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display=['Title','Description','DateTime_of_todo_task','Status','Created','Modified']
    list_filter=('DateTime_of_todo_task','Status','Created')
    search_fields=('Titile','Description')
    actions=["export_as_csv"]
admin.site.register(todo_list,todo_listAdmin)
