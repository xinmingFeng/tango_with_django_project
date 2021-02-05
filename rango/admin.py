from django.contrib import admin
from rango.models import Category,Page



class PageAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','views','likes')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)