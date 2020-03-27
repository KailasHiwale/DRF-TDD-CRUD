from django.contrib import admin

from .models import Institute, Reviewer, Review


admin.site.register(Institute)
admin.site.register(Reviewer)
admin.site.register(Review)