from django.contrib import admin

from gestor.models import Clients, Items, Req

# Register your models here.

admin.site.register(Clients)
admin.site.register(Items)
admin.site.register(Req)