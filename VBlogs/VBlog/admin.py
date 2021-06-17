from django.contrib import admin
from . models import Post, Categories, Profile, Comment, Thoughts

admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Thoughts)

# Register your models here.


