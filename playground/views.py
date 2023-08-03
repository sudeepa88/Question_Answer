from django.shortcuts import get_object_or_404, render

from .models import Question,Choice
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse


class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name="latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("pk")
        


# def detail(request,question_id):
#     try:
#         question=Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question Does not Exist")
#     return render(request,"polls/detail.html",{"question":question})

#/polls/5/ 
class DetailView(generic.DetailView):
    model=Question
    template_name="polls/detail.html"

class ResultsView(generic.DetailView):
    model=Question
    template_name="polls/results.html"

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
         #request.POST is a dictionary-like object that lets you access submitted 
         # data by key name. 
         # In this case, request.POST['choice'] returns the ID 
         # of the selected choice, as a string. 
         # request.POST values are always strings.
    except(KeyError, Choice.DoesNotExist):
        return render(request,"polls/detail.html",{"question":question,"error_message":"You didnot select a choice",},)
    else:
     selected_choice.votes +=1
     selected_choice.save()
     return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))

