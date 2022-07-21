from django.contrib import admin
from .models import Helmet, Motorcycle, Washing

# Register your models here.
admin.site.register(Motorcycle)
admin.site.register(Washing)
admin.site.register(Helmet)