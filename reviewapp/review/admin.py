from django.contrib import admin

from .models import Institute


class InstituteAdmin(admin.ModelAdmin):
    """ Custom admin interface for `Institute` model """
    list_display = (
        'institute_name',
        'address',
        'pin_code',
        'office_mail',
        'phone_number',
        'website',
        'institute_type',
        'founded_in',
        'affiliated_to',
        'approved_by',
        'owner',
    )
    list_display_links = ('institute_name', 'website',)
    list_editale = ('address',)
    list_filter = ('institute_type', 'affiliated_to', 'approved_by',)
    search_fields = ('institute_name',)


admin.site.register(Institute, InstituteAdmin)