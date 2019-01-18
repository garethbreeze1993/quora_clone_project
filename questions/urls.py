from django.urls import path
from questions import views

app_name = 'questions'

urlpatterns = [
	path('<slug>/',views.QuestionDetail.as_view(), name='question_single'),
	path('<slug>/delete/', views.DeleteQuestion.as_view(), name='delete_question'),
	path('<slug>/update/', views.UpdateQuestion.as_view(), name='update_question'),
	path('remove/answer/<pk>/', views.DeleteAnswer.as_view(), name='remove_answer'),

	
]

