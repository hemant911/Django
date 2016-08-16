from django.shortcuts import render

# Create your views here
from django.http import HttpResponse

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." %question_id)

def results(request,question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id )


def vote(request,question_id):
    return HttpResponse("You are voting on questions %s."% question_id)


def index(request):
    return HttpResponse("Hello,world. you are at the polls index.")


