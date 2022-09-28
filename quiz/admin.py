from django.contrib import admin
from .models import QuizModels, UserInfoModel
# Register your models here.

admin.site.register(QuizModels)
admin.site.register(UserInfoModel)
