import re
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import QuizModels, UserInfoModel
from .forms import UserForm
# Create your views here.


class SiginView(View):
    def get(self, request):
        form = UserForm()
        return render(request, "quiz/signin.html", {"form": form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                search_user = UserInfoModel.objects.get(
                    user_name=form.cleaned_data['user_name'])
                if search_user.user_name == form.cleaned_data['user_name']:
                    msg = "Username In Use!"
                    return render(request, "quiz/signin.html", {"form": form, "msg": msg})
            except:
                form.save()
                return HttpResponseRedirect(reverse('login_page'))

        return render(request, "quiz/signin.html", {"form": form})


class LoginView(View):
    def get(self, request):
        return render(request, "quiz/login.html")

    def post(self, request):
        try:
            search_for_user = UserInfoModel.objects.get(
                user_name=request.POST.get('name').lower())
            if search_for_user.password == request.POST.get('password'):
                return HttpResponseRedirect("doroste")
            else:
                msg = "User Doesn't Exist"
                return render(request, "quiz/login.html", {"msg": msg})

        except:
            msg = "User Doesn't Exist"
            return render(request, "quiz/login.html", {"msg": msg})


# def Quiz(request):
#     pass
