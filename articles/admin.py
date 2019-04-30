from django.contrib import admin

from django.contrib import admin
from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'entryDate', 'modificationDate', 'author')
    search_fields = ('title',)
    list_filter = ('title', 'entryDate', 'modificationDate',)


# class CommentInline(admin.TabularInline):model = models.Comment
class CommentInline(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]


admin.site.register(Article, ArticleAdmin)

admin.site.register(Comment)