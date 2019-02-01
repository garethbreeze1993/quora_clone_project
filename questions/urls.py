from django.urls import path
from questions import views

app_name = 'questions'

urlpatterns = [
	path('<slug>/',views.QuestionDetail.as_view(), name='question_single'),
	path('<slug>/delete/', views.DeleteQuestion.as_view(), name='delete_question'),
	path('<slug>/update/', views.UpdateQuestion.as_view(), name='update_question'),
	path('remove/answer/<pk>/', views.DeleteAnswer.as_view(), name='remove_answer'),
	path('<slug>/solved', views.question_solved, name='question_solved'),
	path('answer/<pk>/upvote', views.upvote, name ='upvote'),
	path('answer/<pk>', views.DetailAnswer.as_view(), name='ans_single'),
	path('results/', views.SearchQuests.as_view(), name="search_quests"),

	
]

