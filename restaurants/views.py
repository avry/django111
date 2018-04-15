from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required #for function-based views
from django.contrib.auth.mixins import LoginRequiredMixin #for class-based views
# Create your views here.

from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


#Function-based views
@login_required(login_url='/login/')
def restaurant_createview(request):
	form = RestaurantLocationCreateForm()
	if request.method == "POST":
		form = RestaurantLocationCreateForm(request.POST)
		if form.is_valid():
			if request.user.is_authenticated():
				instance=form.save(commit=False)
				instance.owner = request.user
				instance.save()

				# obj = RestaurantLocation.objects.create(
				# 		name = form.cleaned_data.get('name'), 
				# 		location = form.cleaned_data.get('location'),
				# 		category = form.cleaned_data.get('category')
				# 	)
				return HttpResponseRedirect("/restaurants")
			else:
				return HttpResponseRedirect("/login/")
		if form.errors:
			print(form.errors)
		
	template_name = 'restaurants/form.html'
	context = {"form": form}
	return render(request, template_name, context)


def restaurant_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)




#Generic View
class RestaurantListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

	# def get_context_data(self, *args, **kwargs):
	# 	print(self.kwargs)
	# 	context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation, id=rest_id)
	# 	return obj

class RestaurantCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	login_url = '/login/' #can also set this in settings.py with LOGIN_URL = '/login/' This however is overwritten by anything in the views.py
	template_name = 'form.html'
	# success_url = "/restaurants/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		# instance.save()
		return super(RestaurantCreateView, self).form_valid(form)
 
	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Restaurant'
		return context 


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestaurantLocationCreateForm
	login_url = '/login/' #can also set this in settings.py with LOGIN_URL = '/login/' This however is overwritten by anything in the views.py
	template_name = 'restaurants/detail_update.html'
	# success_url = "/restaurants/"


	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
		name = self.get_object().name
		context['title'] = 'Update Restaurant: {name}'
		return context 


	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)




class HomeView(TemplateView):
	template_name = 'home.html'


class AboutView(TemplateView):
	template_name = 'about.html'


class ContactView(TemplateView):
	template_name = 'contact.html'