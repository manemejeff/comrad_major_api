from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import PollQuestion, PollChoice


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return PollQuestion.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = PollQuestion
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = PollQuestion
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(PollQuestion, pk=question_id)
    try:
        selected_choice = question.pollchoice_set.get(pk=request.POST['choice'])
    except(KeyError, PollChoice.DoesNotExist):
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': 'You didn`t select a choice',
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
