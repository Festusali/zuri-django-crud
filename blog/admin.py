from django.contrib import admin

# Import Post model
from blog.models import Post


# Register Post model in the Django admin panel
admin.site.register(Post)
