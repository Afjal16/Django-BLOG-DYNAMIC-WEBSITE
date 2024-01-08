from django.contrib import admin
from blog.models import Category,Post,Tag,Contact,Comment,Author_name

# Register your models here.

class TagTublerInline(admin.TabularInline):
    model=Tag
    
class AuthorTublerInline(admin.TabularInline):
    model=Author_name
    
class PostAdmin(admin.ModelAdmin):
    inlines=[TagTublerInline, AuthorTublerInline]
    list_display=['title','author','date','status','category','section','main_post']
    list_editable=['status','section','main_post']
    prepopulated_fields= {'slug':('title',)}
    
    
class ContactAdmin(admin.ModelAdmin):
    list_display=['username','email','subject','message']
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'post', 'created_date', 'active')
    list_filter = ('active', 'created_date')
    search_fields = ('user', 'text')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Category)
admin.site.register(Author_name)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Comment,CommentAdmin)