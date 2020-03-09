from django.contrib import admin
from django .contrib.auth.admin import UserAdmin
from .models import Post, Comment


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined',
                    'last_login', 'is_admin', 'is_staff')
    search_field = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(AccountAdmin)
