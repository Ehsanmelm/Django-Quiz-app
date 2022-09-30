from django.contrib import admin
from .models import QuizModels, UserInfoModel, QuizResulModel
# Register your models here.

admin.site.register(QuizModels)
admin.site.register(UserInfoModel)
admin.site.register(QuizResulModel)
