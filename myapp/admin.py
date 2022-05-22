from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}


admin.site.register(Articles)
admin.site.register(Myvideo)
admin.site.register(MenPrize)
admin.site.register(Tokyo)
admin.site.register(Summer)
admin.site.register(Winter)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)