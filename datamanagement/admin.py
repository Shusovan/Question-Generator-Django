from django.contrib import admin # type: ignore
from .models import Question

# Register your models here.
admin.site.register(Question)

