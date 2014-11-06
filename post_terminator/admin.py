import reversion
from django.contrib import admin
from biblion.models import Post
from biblion.admin import PostAdmin


class VersionedPostAdmin(reversion.VersionAdmin, PostAdmin):
    pass


admin.site.unregister(Post)
admin.site.register(Post, VersionedPostAdmin)
