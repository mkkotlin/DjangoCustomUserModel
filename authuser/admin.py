from django.contrib import admin
from authuser.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('password',)


admin.site.register(User,UserAdmin)