from  django.contrib import admin
from .models import Author, ContactUsRequest, ContactUs, FAQ, Post, Category, Tag



class BaseModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    list_display_links = ['title']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-updated_at']
    
    class Meta:
        abstract=True


@admin.register(FAQ)
class FAQAdmin(BaseModelAdmin):
    list_display = ['question', 'answer', 'created_at', 'updated_at']
    list_display_links = ['question']


@admin.register(ContactUsRequest)
class ContactUsRequestAdmin(BaseModelAdmin):
    list_display = ['name', 'subject', 'created_at', 'updated_at']
    list_display_links = ['name']
    
    
@admin.register(Post)
class PostAdmin(BaseModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    date_hierarchy = 'updated_at'
    
    
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Author)
class AuthorAdmin(BaseModelAdmin):
    pass
    
    
@admin.register(Category)
class CategoryAdmin(BaseModelAdmin):
    pass
    
    
@admin.register(Tag)
class TagAdmin(BaseModelAdmin):
    pass