from django.contrib import admin
# import class yang dibutuhkan untuk memodifikasi form pada User Admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
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


# Membuat Custom Form untuk Form Add User
class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', )


# Membuat Custom Form untuk Form Update User
class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', )
        
        
# Mengeset Custom User Form ke modul User Admin
class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = UserUpdateForm
    prepopulated_fields = {'username': ('first_name', 'last_name', )}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', ),
        }),
    )
    
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'username', ),
        }),
    )


# Mendaftarkan ulang User Admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)