import re
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

import quiz
from .models import QuizModels, UserInfoModel, QuizResulModel
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
#     passc

class QuizView(View):
    def get(self, request):
        questions = QuizModels.objects.all()
        return render(request, "quiz/quiz.html", {"questions": questions})

    def post(self, request):
        questions = QuizModels.objects.all()
        chosen_option = []
        wrong_answer_dict = {}
        score = 0
        wrong_answer = 0
        for i in range(len(questions)):
            chosen_option.append(request.POST.get(str(questions[i].id)))
        for loop_counter, i in enumerate(questions):
            print(chosen_option[loop_counter], i.answer)
            if i.answer == chosen_option[loop_counter]:
                score += 10
            else:
                wrong_answer_dict[loop_counter+1] = i.answer
                wrong_answer += 1
        msg = f"You'r score: {score}   wrong answers: {wrong_answer}"
        return render(request, "quiz/quiz.html", {"questions": questions, "msg": msg, "wrong_answers": wrong_answer_dict.items()})

        # chosen_option = request.POST.get(str(questions[0].id))
        # question_id = request.POST.get('question_id')
        # quiz_model = QuizModels.objects.get(id=question_id)

        # if chosen_option == quiz_model.answer:
        #     msg = "very good :))"
        # else:
        #     msg = "wrong answer!"
        # print(f"chosen_option:{chosen_option}    answer:{quiz_model.answer}")
