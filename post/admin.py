from django.contrib import admin

# Register your models here.
from post.models import Topic, Comment

#admin.site.register([Topic, Comment])
class TopicAdmin(admin.ModelAdmin):
    pass
class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)