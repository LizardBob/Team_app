from django.contrib import admin
from .models import Teams, Users
# Register your models here.

# class TeamsAdmin(admin.ModelAdmin):
#     fields = ['idteam', 'team_name']
#     list_display = ('idteam', 'team_name')
#     list_filter = ['team_name']
#     search_fields = ['idteam', 'team_name']
#
# class UsersAdmin(admin.ModelAdmin):
#     fields = ['iduser', 'user_mail', 'password', 'role', 'user_name', 'user_surname', 'idteam']
#     list_display = ('iduser', 'user_mail', 'password', 'role', 'user_name', 'user_surname', 'idteam')
#     list_filter = ['user_name', 'user_surname', 'user_mail']
#     search_fields = ['iduser', 'user_mail', 'role', 'user_name', 'user_surname', 'idteam']
# admin.site.register(Teams, TeamsAdmin)
# admin.site.register(Users, UsersAdmin)
admin.site.register(Teams)
admin.site.register(Users)
