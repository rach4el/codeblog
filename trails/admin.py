from django.contrib import admin
from .models import CreatePost
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(CreatePost)
class CreatePostAdmin(admin.ModelAdmin):

    list_display = ('approved', 'updated_on', 'creator', 'title', 'slug', 'created_on', 'suggested_riding_ability', 'county')
    search_fields = ['title', 'content', 'county']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    readonly_fields = ('created_on',)