from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_superuser", "is_active",)
    list_filter = ("email", "is_superuser", "is_active",)
    search_fields = ("email",)
    ordering=('email',)

    fieldsets = (
        ('Authentications', {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Group Permissions", {"fields": ("groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active",  "is_superuser"
            )}
        ),
    )

class CustomProfileAdmin(ModelAdmin):
    model = Profile
    list_display = ("user", "first_name", "last_name",)
    list_filter = ("user", "first_name", "last_name",)
    ordering = ('user__email',)  # Order by user's email instead of username
    readonly_fields = ("created_date", "updated_date")

    fieldsets = (
        ('Profile Information', {"fields": ("user", "first_name", "last_name","image","description")}),
        ("Important Dates", {
            "fields": ("created_date", "updated_date"),
            # "classes": ("collapse",)  # Optional: makes the section collapsible
        }),
    )


admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile,CustomProfileAdmin)