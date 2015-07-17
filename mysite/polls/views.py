from django.shortcuts import get_object_or_404, render

from django.http import Http404

from django.http import HttpResponseRedirect, HttpResponse
#if you comment the above line, index will work but not others
from .models import Question, Choice

from django.core.urlresolvers import reverse

from django.views import generic

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


def vote(request, question_id):
 	p = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question' : p,
			'error_message' : "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
		

	#6.return HttpResponse("You're voting on question %s." % question_id)

