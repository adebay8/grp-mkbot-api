from django.contrib import admin
from .models import Store, Category, StoreNode

# Register your models here.

admin.site.register([Store, Category, StoreNode])
