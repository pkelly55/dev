from django.contrib import admin
from .models import Record , Monitor, CPU_load, bad_IP 


# Register your models here.

admin.site.register(Record)
admin.site.register(Monitor)
admin.site.register(CPU_load)
admin.site.register(bad_IP)