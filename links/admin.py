from django.contrib import admin
from .models import Link, Tag


class LinkAdmin(admin.ModelAdmin):
    list_filter = ('approved',)


admin.site.register(Link, LinkAdmin)
admin.site.register(Tag)
