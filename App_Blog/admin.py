from django.contrib import admin
from .models import Blog, Comment, Likes, Catagory

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ["author", "blog_title", "blog_content", "publish_date"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "blog", "comment", "comment_date"]


class LikesAdmin(admin.ModelAdmin):
    list_display = ["user", "blog"]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Likes, LikesAdmin)
admin.site.register(Catagory)
