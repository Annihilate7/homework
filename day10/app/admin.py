from django.contrib import admin

from app import models

admin.site.register(models.Book)
admin.site.register(models.Press)
admin.site.register(models.Author)
admin.site.register(models.AuthorDetail)
admin.site.register(models.User)