from django.contrib import admin
# import class model Category
from .models import Category


# Menambahkan modul Category ke Admin
class CategoryAdmin(admin.ModelAdmin):
    # Menampilkan kolom "name" dan "created_at" pada halaman Category list di Admin
    list_display = ('name', 'created_at')
    # Menambahkan fitur pencarian berdasarkan kolom "name"
    search_fields = ['name']


# Mendaftarkan CategoryAdmin
admin.site.register(Category, CategoryAdmin)