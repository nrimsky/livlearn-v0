from django.contrib import admin
from .models import Link, Tag
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class LinkResource(resources.ModelResource):
    class Meta:
        model = Link


@admin.register(Link)
class LinkAdmin(ImportExportModelAdmin):
    list_filter = ('approved',)
    resource_class = LinkResource


admin.site.register(Tag)
