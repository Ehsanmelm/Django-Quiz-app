from django.contrib import admin
from .models import QuizModels, UserInfoModel, QuizResulModel
# Register your models here.


class UserInfoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("email", )}
    list_display = ("user_name", )


class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score')


admin.site.register(QuizModels)
admin.site.register(UserInfoModel, UserInfoAdmin)
admin.site.register(QuizResulModel, QuizResultAdmin)
