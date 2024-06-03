from django.contrib import admin
from FormData.models import CustomerInfo

# Register your models here.
@admin.register(CustomerInfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','password')