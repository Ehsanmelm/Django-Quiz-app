from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.utils.text import slugify
from .models import QuizModels, UserInfoModel, QuizResulModel
from .forms import UserForm
# Create your views here.


class SiginView(View):
    def get(self, request):
        form = UserForm()
        return render(request, "quiz/signin.html", {"form": form})

    def post(self, request):
        form = UserForm(request.POST)
        if form .is_valid():
            users = UserInfoModel.objects.values("user_name", "password")
            for i in users:
                if form.cleaned_data['user_name'] == i["user_name"] and form.cleaned_data['password'] == i["password"]:
                    msg = "username has already in use"
                    print("mordammmmm")
                    return render(request, "quiz/signin.html", {"form": form, "msg": msg})
            else:
                quiz_slug = form.save(commit=False)
                quiz_slug.slug = slugify(quiz_slug.email)
                quiz_slug.save()
                return HttpResponseRedirect(reverse('login_page'))

        return render(request, "quiz/signin.html", {"form": form})


class LoginView(View):
    def get(self, request):
        return render(request, "quiz/login.html", {"is_sign_in": True})

    def post(self, request):

        try:
            find_user = UserInfoModel.objects.get(user_name=request.POST.get(
                'name'), password=request.POST.get('password'))
            # is_sign_in = True
            request.session['loged_in_user'] = find_user.id
            return HttpResponseRedirect('quiz/' + find_user.slug)
        except:
            msg = "User Doesn't Exist"
            is_sign_in = False
            return render(request, "quiz/login.html", {"msg": msg, "is_sign_in ": is_sign_in})


class QuizView(View):
    def get(self, request, slug):
        questions = QuizModels.objects.all()
        return render(request, "quiz/quiz.html", {"questions": questions})

    def post(self, request, slug):
        questions = QuizModels.objects.all()
        chosen_option = []
        wrong_answer_dict = {}
        score = 0
        wrong_answer = 0
        num_of_questions = QuizModels.objects.all().count()
        for i in range(len(questions)):
            chosen_option.append(request.POST.get(str(questions[i].id)))
        for loop_counter, i in enumerate(questions):
            print(chosen_option[loop_counter], i.answer)
            if i.answer == chosen_option[loop_counter]:
                score += 100/num_of_questions
            else:
                wrong_answer_dict[loop_counter+1] = i.answer
                wrong_answer += 1
        msg = f"You'r score: {score}   wrong answers: {wrong_answer}"

        # saving quiz result in database
        loged_in_user_id = request.session.get('loged_in_user')
        participated_user = UserInfoModel.objects.get(id=loged_in_user_id)
        quiz_result = QuizResulModel(score=score, user=participated_user)
        quiz_result.save()

        return render(request, "quiz/quiz.html", {"questions": questions, "msg": msg, "wrong_answers": wrong_answer_dict.items(), "is_done": True})
