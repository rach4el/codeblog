from django.contrib import admin
from .models import ContactUs

# Contact us class requests appear in admin with authory unchangable from origin

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('query_title', 'author', 'created_on', 'resolved', 'updated_on')
    list_filter = ('resolved',)
    search_fields = ('query_title', 'content', 'author__username')
    readonly_fields = ('author',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Author field set upon origin.
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(ContactUs, ContactUsAdmin)