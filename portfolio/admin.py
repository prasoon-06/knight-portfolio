from django.contrib import admin
from .models import SiteProfile, Project
@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ("display_name", "college")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech_stack", "sort_order")
    list_editable = ("sort_order",)
    ordering = ("sort_order", "title")

# Register your models here.
from .models import HobbyImage
@admin.register(HobbyImage)
class HobbyImageAdmin(admin.ModelAdmin):
    list_display = ("title", "sort_order")
    list_editable = ("sort_order",)

from .models import ChapterImage

@admin.register(ChapterImage)
class ChapterImageAdmin(admin.ModelAdmin):
    list_display = ("chapter", "sort_order")
    list_editable = ("sort_order",)
    ordering = ("chapter", "sort_order")
