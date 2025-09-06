from django.contrib import admin

# Register your models here.
from apps.movies.models import *



admin.site.register(Movie)
admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(MovieAudio)
admin.site.register(MovieFile)
admin.site.register(MovieSubtitle)
admin.site.register(Posterlmage)