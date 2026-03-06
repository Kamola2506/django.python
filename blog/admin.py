from django.contrib import admin
from .models import Post , Feedback
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','created_at','updated_at')
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name','email','question','created_at','answer','updated_at','answered_by')
