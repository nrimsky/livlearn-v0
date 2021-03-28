from django.contrib import admin
from .models import Link, Tag, Comment
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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    def user(self, comment):
        return comment.user.username

    def link(self, comment):
        return comment.link.name

    list_display = ('id', 'user', 'link', 'created_on', 'body')
    search_fields = ('body', 'user', 'link')