from .models import UserNumber, ImageVerifaction
from django.contrib import admin

# Register your models here.


class UserNumberAdmin(admin.ModelAdmin):
    list_display = ['user', 'number']

    class Meta:
        model = UserNumber


class ImageVerifactionAdmin(admin.ModelAdmin):
    list_display = ['user']

    class Meta:
        model = ImageVerifaction


admin.site.register(UserNumber, UserNumberAdmin)
admin.site.register(ImageVerifaction, ImageVerifactionAdmin)
