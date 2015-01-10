from django.contrib import admin
from mysite import models
# Register your models here.


class SignupAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'myclass', 'email')
    search_fields = ('fullname', 'myclass')


class UserAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'num', 'email')
    search_fields = ('fullname', 'num')

admin.site.register(models.Content)
admin.site.register(models.Center)
admin.site.register(models.RContent)
admin.site.register(models.JoinMe, SignupAdmin)
admin.site.register(models.Project)
admin.site.register(models.Activities)
admin.site.register(models.User, UserAdmin)
