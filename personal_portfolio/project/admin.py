from django.contrib import admin
from django.utils.html import format_html
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    def project_photo(self, object):
        return format_html('<img src= "{}" width= "100"/>'.format(object.image.url))

    list_display = ('project_photo','title', 'technology')
    list_display_links = ('title','project_photo')

admin.site.register(Project, ProjectAdmin)
