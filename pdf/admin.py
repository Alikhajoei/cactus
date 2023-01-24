from django.contrib import admin
from .models import Genre, Book, NewsEmail


class GenreAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'slug')
	list_filter = ('name', 'slug')

	fieldsets = ((None, {'fields': ('icon', 'name', 'slug',)}),)
	add_feildsets = ((None, {'classes': ('wide',),
							 'fields': ('icon', 'name', 'slug',)}),)

	ordering = ('id',)
	search_fields = ('name',)



# class PdfAdmin(admin.ModelAdmin):

# 	list_display = ('title', 'genre', 'writer')
# 	list_filter = ('writer', 'genre')

# 	fieldsets = ((None, {'fields': ( 'title', 'genre', 'writer', 'file')}),)
# 	add_fieldsets = ((None, {'classes': ('wide',),
# 								'fields': ( 'title', 'genre', 'writer', 'file')}),)

# 	search_fields = ('title', 'genre', 'writer')
# 	ordering = ('title',)


class NewsEmailAdmin(admin.ModelAdmin):
	list_display = ('ip', 'email', 'joined_date')
	list_filter = ('joined_date', )

	fieldsets = ((None, {'fields': ('ip', 'email', 'joined_date')}),)
	add_fieldsets = ((None, {'classes': ('wide',),
							 'fiedls': ('ip', 'email', 'joined_date')}),)
	ordering = ('ip',)
	search_fields = ('ip', 'email',)



admin.site.register(Book)
admin.site.register(Genre, GenreAdmin)
admin.site.register(NewsEmail, NewsEmailAdmin)