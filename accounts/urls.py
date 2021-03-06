from django.urls import path
from django.contrib.auth import views as auth_views # djangos built in auth
from accounts import views
from questions import views as v

app_name = 'accounts'

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name= "accounts/login.html"), name='login'), # same as last project
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('signup/', views.Signup.as_view(), name='signup'),
	path('<slug>/', v.UserProfileQuestion, name = 'profile'),
	#path('<slug>/', v.UserProfile.as_view(), name='profile'),
]
