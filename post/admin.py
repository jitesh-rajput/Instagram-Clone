from django.contrib import admin
from . models import Post,like,comment
# Register your models here.

admin.site.register(Post)
admin.site.register(like)
admin.site.register(comment)