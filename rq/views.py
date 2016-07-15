from django.shortcuts import render
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from .models import Question
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from .tasks import assignQuestion

# Create your views here.
@login_required
def home(request):
	if request.method == "POST":
		if request.is_ajax():
			qpk = request.POST['q']
			ans = request.POST['answer']
			data = {"qpk":qpk, "ans":ans}
			q = Question.objects.get(pk=qpk)
			q.a = ans
			q.save()
			return JsonResponse(data)
	else:
		qs_con = []
		qs = Question.objects.filter(assignee=request.user).order_by('-cdt')
		for q in qs:
			qs_con.append(q)
		return render(request,'rq/home.html', {'qs': qs_con, 'nbar':'home'})

@login_required
def submitq(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if not form.is_valid():
			return render(request, 'rq/submit.html', {'form': form})
		q=Question(q=request.POST['q'], asker=request.user)
		q.save()
		assignQuestion.delay(q)
		return HttpResponseRedirect(reverse('rq:aq'))
	else:
		form = QuestionForm()
		return render(request, 'rq/submit.html', {'form': form, 'nbar':'sq'})

@login_required
def asked(request):
	aqs_con = []
	aqs = Question.objects.filter(asker=request.user).order_by('-cdt')
	for q in aqs:
		aqs_con.append(q)
	return render(request, 'rq/asked.html', {'aqs': aqs_con, 'nbar':'aq'})
