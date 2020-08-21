from django.contrib import admin
from posts.models import Post
from posts.models import Comments

admin.site.register(Post)
admin.site.register(Comments)