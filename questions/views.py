from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin
from django.core.paginator import Paginator
from questions.models import Question, Answer
from accounts.models import User
from questions.forms import QuestionForm, AnswerForm
from django.http import Http404
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()


class QuestionList(ListView):
	model = Question
	#template_name = 'questions/_question.html'
	
class QuestionDetail(FormMixin,DetailView):
	model = Question
	form_class = AnswerForm
	
	def get_success_url(self):
		return reverse('questions:question_single', kwargs={'slug': self.object.slug})
		
	def get_context_data(self, **kwargs):
		context = super(QuestionDetail, self).get_context_data(**kwargs)
		context['form'] = AnswerForm(initial={'question': self.object, 'author':self.request.user})
		return context	
	
	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
			
	def form_valid(self, form):
		form.save()
		return super(QuestionDetail, self).form_valid(form)		
	
	
class CreateQuestion(LoginRequiredMixin, CreateView):
	model = Question
	form_class = QuestionForm
	
	def form_valid(self,form):
		self.object = form.save(commit=False)
		self.object.author = self.request.user # connect post to a user
		self.object.save()
		return super().form_valid(form)
		
		
	
class DeleteQuestion(LoginRequiredMixin, DeleteView):
	model = Question
	success_url = reverse_lazy('home')
	
class UpdateQuestion(LoginRequiredMixin,UpdateView):
	model = Question
	form_class = QuestionForm
	template_name_suffix = '_update_form'
	
class DeleteAnswer(LoginRequiredMixin, DeleteView):
	model = Answer
	success_url = reverse_lazy('home')
	
class DetailAnswer(DetailView):
	model = Answer
	template_name = 'questions/answer_detail.html'

def SearchQuests(request):
	if request.method == 'GET':
		query = request.GET.get('q')
		
		results = Question.objects.filter(name__icontains=query)
	
		return render(request,'questions/question_list.html',{'results':results})
	else:
		return render(request,'questions/question_list.html')
		
	
	
	

def UserProfileQuestion(request, slug):
	user = User.objects.get(slug=slug)
	user_question = Question.objects.filter(author=user).order_by('-created_date')
	paginator = Paginator(user_question, 2)
	page = request.GET.get('page')
	questions = paginator.get_page(page)
	
	user_answer = Answer.objects.filter(author=user).order_by('-created_date')
	
	paginatorAnswer = Paginator(user_answer, 3)
	pageAns = request.GET.get('page2')
	answers = paginatorAnswer.get_page(pageAns)
	
	
	return render(request,'questions/user_profile2.html',{'user_question':questions,'user_answer':answers,'user': user})

@login_required
def question_solved(request,slug):
	question = get_object_or_404(Question,slug=slug)
	question.question_solved()
	return redirect('questions:question_single',slug=question.slug)

@login_required	
def upvote(request,pk):
	answer = get_object_or_404(Answer, pk=pk)
	answer.likes += 1
	answer.save()
	return redirect('questions:question_single',slug=answer.question.slug)	
	
	

		
			
	
	


	
