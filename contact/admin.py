from django.contrib import admin
from .models import ContactUs

# Contant us admin view, author and created on fields set upon submission

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('query_title', 'author', 'created_on', 'resolved', 'updated_on', 'admin_response')
    list_filter = ('resolved',)
    search_fields = ('query_title', 'content', 'author__username')
    readonly_fields = ('author',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(ContactUs, ContactUsAdmin)