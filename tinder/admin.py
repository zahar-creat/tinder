from django.contrib import admin
from .models import Users, Project, Image, Choice


# Register your models here.
admin.site.register(Image)


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1


@admin.register(Users)
class Useradmin(admin.ModelAdmin):
    inlines = (ChoiceInLine)


@admin.register(Project)
class Projectadmin(admin.ModelAdmin):
    inlines = (ChoiceInLine)
