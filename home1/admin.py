from django.contrib import admin

from home1.models import Book, Author, Genre, Student

# Register your models here.

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('id','name')
    #efields = [('name','purchase_date'),('genre','book_author')]
    list_filter = ('purchase_date','name',('book_author',admin.RelatedOnlyFieldListFilter))

@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('s_name','name')
    #list_filter = ('s_name','name')
