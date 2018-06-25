# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = 'rango/index.html'

	def get_context_data(self):
		context = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
		return context

class AboutView(TemplateView):
	template_name = 'rango/about.html'

	def get_context_data(self):
		context = {'name': "Dan Flath"}
		return context