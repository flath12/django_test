# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from rango.models import Category

class IndexView(TemplateView):
	template_name = 'rango/index.html'

	def get_context_data(self):
		category_list = Category.objects.order_by('-likes')[:5]
		context = {'categories': category_list}
		return context

class AboutView(TemplateView):
	template_name = 'rango/about.html'

	def get_context_data(self):
		context = {'name': "Dan Flath"}
		return context