from operator import imod
from django.contrib import admin
from users.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'last_login', 'is_staff', 'is_active']
    list_filter = ('is_staff',)
    ordering = ('last_login',)
    exclude = ('password', )
    resource_class = User

admin.site.register(User, UserAdmin)