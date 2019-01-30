from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormMixin
from questions.models import Question, Answer
from accounts.models import User
from questions.forms import QuestionForm, AnswerForm
from django.http import Http404
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
	

def UserProfileQuestion(request, slug):
	user = User.objects.get(slug=slug)
	user_question = Question.objects.filter(author=user).order_by('-created_date')
	user_answer = Answer.objects.filter(author=user).order_by('-created_date')
	return render(request, 'questions/user_profile.html', {'user_question':user_question,'user_answer':user_answer, 'user': user})

@login_required
def question_solved(request,slug):
	question = get_object_or_404(Question,slug=slug)
	question.question_solved()
	return redirect('questions:question_single',slug=question.slug)

	
	
	
'''
class UserProfile(DetailView):	
	template_name = 'questions/user_profile.html'
	model = User
	#slug_url_kwarg = 'slug'
	#userr = User.objects.get(slug=slug_url_kwarg)
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		slug = self.kwargs['slug']
		context['userr'] = User.objects.get(slug)
		context['user_quest'] = Question.objects.filter(author=User.objects.get(slug)).order_by('-created_date')
		context['user_ans'] = Answer.objects.filter(author=User.objects.get(slug)).order_by('-created_date')		
		return context
'''			
			
	
	


	
