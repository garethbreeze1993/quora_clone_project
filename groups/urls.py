from django.urls import path
from groups import views

app_name = 'groups'

urlpatterns = [
	path('<slug>/',views.GroupDetail.as_view(), name='single'),
	
]
