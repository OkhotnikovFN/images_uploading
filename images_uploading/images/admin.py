from django.contrib import admin

from images import models


@admin.register(models.Image)
class NewsAdmin(admin.ModelAdmin):
    pass
