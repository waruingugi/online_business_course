from django.contrib import admin
from registration.models import Users
from django.contrib.auth.models import Group


class UsersPage(admin.ModelAdmin):
    list_display = ('subscribed_date', 'username', 'email')
    search_field = ['username', 'email']


admin.site.register(Users, UsersPage)
admin.site.unregister(Group)
