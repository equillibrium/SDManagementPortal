from django.contrib import admin

from NewADUser.models import NewADUser

from ManageADUsers.models import ADUser


admin.site.register(NewADUser)
admin.site.register(ADUser)
