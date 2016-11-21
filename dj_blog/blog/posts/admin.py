from django.contrib import admin
from .models import Post
# Register your models here.

class AdminModel(admin.ModelAdmin):
    list_display = ['title','updated','timestamp']
    #change link i admin panel
    #list_display_link=[]
    list_filter=['updated','timestamp']
    search_fields = ['title','content']
    class Meta:
        model = Post

admin.site.register(Post, AdminModel)