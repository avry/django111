from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
# Create your views here.




# #function-based view
# def home(request):
# 	# return HttpResponse("hello")
# 	return render(request, "home.html", {})


# def contact(request):
# 	# return HttpResponse("hello")
# 	return render(request, "contact.html", {})


# def about(request):
# 	# return HttpResponse("hello")
# 	return render(request, "about.html", {})


# class ContactView(View):
# 	def get(self, request, *args, **kwargs):
# 		context = {}
# 		return render(request, "contact.html", context)


class HomeView(TemplateView):
	template_name = 'home.html'


class AboutView(TemplateView):
	template_name = 'about.html'


class ContactView(TemplateView):
	template_name = 'contact.html'