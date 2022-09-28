from dataclasses import fields
from django import forms
from .models import UserInfoModel, QuizModels


class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfoModel
        fields = '__all__'
