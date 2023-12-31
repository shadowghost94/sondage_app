from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }

    return render(request, "polls/index.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        Question.DoesNotExist
        raise Http404("La question n'existe pas")
    
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "Vous consulter le résultat de la question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Vous votez pour la question %s." % question_id)