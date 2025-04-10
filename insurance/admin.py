from django.contrib import admin

# Register your models here.

from .models import Customer
from insurance.models import Category,Policy,PolicyRecord,Question

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Policy)
admin.site.register(PolicyRecord)
admin.site.register(Question)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('customer', 'policy', 'claim_date', 'status')
    list_filter = ('status',)
    search_fields = ('customer__user__username', 'policy__name')