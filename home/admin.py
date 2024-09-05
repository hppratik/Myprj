from django.contrib import admin
from home.models import User
from home.models import Client
from home.models import Project
# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Project)