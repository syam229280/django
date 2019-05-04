from django.contrib import admin
from .models import BillCategory, BillTag, Bill

# Register your models here.
class BillCategoryAdmin(admin.ModelAdmin):
    model = BillCategory
    search_fields = ['category_name']

admin.site.register(BillCategory,BillCategoryAdmin)

class BillTagAdmin(admin.ModelAdmin):
    model = BillTag
    search_fields = ['tag_name']

admin.site.register(BillTag,BillTagAdmin)

class BillAdmin(admin.ModelAdmin):
    model = Bill
    list_display = ('title', 'date', 'category')
    autocomplete_fields = ['tags']

admin.site.register(Bill,BillAdmin)