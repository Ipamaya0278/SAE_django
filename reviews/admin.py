from django.contrib import admin
from .models import Machine, Personnel, Review
from django.contrib.auth.models import Group, User

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review
    extra =0 

class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('num_secu','nom','prenom','infra')
    list_filter = ['nom']
    search_fields = ['num_secu']
    

class MachineAdmin(admin.ModelAdmin) : 
    list_display = ('id','nom','maintenanceDate', 'mach','infra')
    list_filter = ['id','maintenanceDate']
    search_fields = ['nom']


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Personnel, PersonnelAdmin)

 