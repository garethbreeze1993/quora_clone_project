from django.shortcuts import render
from django.views.generic import ListView, DetailView
from groups.models import Group

class GroupList(ListView):
	model = Group
	

class GroupDetail(DetailView):
	model = Group