from django.contrib import admin
from .models import User,Verifycode
# Register your models here.

admin.site.register(User)

admin.site.register(Verifycode)