from django.contrib import admin
from .models import Review, Comment

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'review', )

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)