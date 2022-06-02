from django.contrib import admin
from .models import Dog, Group, Rescue

admin.site.register(Dog) 
admin.site.register(Group)
admin.site.register(Rescue)