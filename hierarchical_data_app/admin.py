from django.contrib import admin

from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from .models import Tree_Model
# Register your models here.

admin.site.register(Tree_Model, DraggableMPTTAdmin)
