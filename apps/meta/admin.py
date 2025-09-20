from django.contrib import admin

from apps.meta.models import Like, WatchSession , Comment


admin.site.register(WatchSession)
admin.site.register(Comment)
admin.site.register(Like)


