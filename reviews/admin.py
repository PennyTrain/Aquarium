from django.contrib import admin
from .models import ReviewPost
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(ReviewPost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status', 'title',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


