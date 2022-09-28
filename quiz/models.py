from cProfile import label
from multiprocessing.connection import answer_challenge
from django.db import models

# Create your models here.


class UserInfoModel(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user_name


class QuizModels(models.Model):
    question = models.TextField()
    opt1 = models.CharField(max_length=255)
    opt2 = models.CharField(max_length=255)
    opt3 = models.CharField(max_length=255)
    opt4 = models.CharField(max_length=255)
    ANSWER_OPTIONS = [
        ("opt1", "opt1"),
        ("opt2", "opt2"),
        ("opt3", "opt3"),
        ("opt4", "opt4"),
    ]
    answer = models.CharField(max_length=255, choices=ANSWER_OPTIONS)
