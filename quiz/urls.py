from . import views
from django.urls import path

urlpatterns = [
    path("signin", views.SiginView.as_view(), name="signin_page"),
    path("login", views.LoginView.as_view(), name="login_page"),
    path("quiz", views.QuizView.as_view(), name="quiz_page"),
]
