from django.contrib import admin
from .models import User, Scheme, Company, Technician

""" Register models """

admin.site.register(User)
admin.site.register(Scheme)
admin.site.register(Company)
admin.site.register(Technician)