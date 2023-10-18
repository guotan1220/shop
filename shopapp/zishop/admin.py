from django.contrib import admin

# Register your models here.
from .models import BookInfo, PeopleInfo
# 将模型类注册到该页面

admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
