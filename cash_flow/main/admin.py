from django.contrib import admin
from .models import *

admin.site.register(Records)
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Type)