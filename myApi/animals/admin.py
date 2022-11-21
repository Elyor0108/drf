from django.contrib import admin

from .models import Animals, Category


@admin.register(Animals)
class Animals(admin.ModelAdmin):
    save_as = True
    save_on_top = True


admin.site.register(Category)
