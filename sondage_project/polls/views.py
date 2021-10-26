from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue sur le sondage !")

def detail(request, question_id):
    return HttpResponse("Vous regardez la question %s." % question_id)

def results(request, question_id):
    response = "Vous regardez le résultat de la question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Vous votez sur la question %s." % question_id)
