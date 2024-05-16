from django.contrib import admin
from ir_app.models import documents
from ir_app.models import invertedindex


# Register your models here.
admin.site.register(documents)
admin.site.register(invertedindex)