
from django.contrib import admin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ('email', 'phone_number', 'is_admin')
	list_filter = ('is_admin',)
	readonly_fields = ('last_login',)

	fieldsets = (
		('Main', {'fields':('username','national_code','email', 'phone_number', 'first_name', 'last_name', 'password', 'birthday_date', 'gender', 'avatar')}),
		('Permissions', {'fields':('is_active', 'is_admin', 'last_login')}),
	)

	add_fieldsets = (
		(None, {'fields':('username','phone_number', 'email', 'first_name', 'password1', 'password2')}),
	)

	search_fields = ('email', 'phone_number')
	ordering = ('last_name',)
	filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User,UserAdmin)