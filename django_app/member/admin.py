from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import MyUser


# 상속받은 User 모델에 img_profile을 추가했으므로, UserAdmin에도 img_profile을 추가하기 위해 fieldset을 재정의.
# 이렇게 해야 admin 화면에 추가된 img_profile 필드가 나타난다.
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'img_profile')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        )


admin.site.register(MyUser, MyUserAdmin)