from django.contrib import admin
from rango.models import Category, Page
# Register your models here.


# Alternatively we could make use of annotations: @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)