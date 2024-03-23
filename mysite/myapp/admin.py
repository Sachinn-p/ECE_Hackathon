from django.contrib import admin
from .models import UserDetails,UserPurpose,LoanRequest

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(UserPurpose)
admin.site.register(LoanRequest)