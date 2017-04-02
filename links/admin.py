from django.contrib import admin
from links.models import Link, Comment


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'submitted_by', 'submitted_on')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'commented_on', 'in_reply_to',
                    'commented_by', 'created_on')


admin.site.register(Link, LinkAdmin)
admin.site.register(Comment, CommentAdmin)
