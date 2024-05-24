from django.contrib import admin
from .models import CreatePost
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(CreatePost)
class CreatePostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)