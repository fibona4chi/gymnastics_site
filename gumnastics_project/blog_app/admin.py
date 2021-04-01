from django.contrib import admin
from .models import ContentPost


class ContentPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


admin.site.register(ContentPost, ContentPostAdmin)