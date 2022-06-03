from django.contrib import admin
from .models import *


class CategoriesInline(admin.TabularInline):
    model = Articles.categories.through
    list_display = ('name',)


class ArticlesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Наименование статьи', {'fields': ['title']}),
        ('Содержание', {'fields': ['content']}),
        ('Дата публикации', {'fields': ['pub_date']}),
        ('Изображение', {'fields': ['image']}),
    ]
    inlines = [
        CategoriesInline
        ]
    readonly_fields = ('categories',)


admin.site.register(Articles, ArticlesAdmin)
