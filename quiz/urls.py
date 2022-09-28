from . import views
from django.urls import path

urlpatterns = [
    path("signin", views.SiginView.as_view(), name="signin_page"),
    path("login", views.LoginView.as_view(), name="login_page"),
    # path("Quiz", views.Quiz, name="quiz_page"),
]
