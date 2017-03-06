from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from analytics.models import ClickEvent

from .models import KirrURL
from .forms import SubmitURLForm
# Create your views here.

class HomeView(View):
	def get(self,request,*args,**kwargs):
		the_form = SubmitURLForm()
		return render(request,'shortner/home.html',{"title": "Kirr Co","form":the_form})

	def post(self,request,*args,**kwargs):
		form = SubmitURLForm(request.POST)
		context = {"title": "Kirr Co","form":form}
		template = 'shortner/home.html'
		if form.is_valid():
			new_url = form.cleaned_data.get("url")
			obj,created = KirrURL.objects.get_or_create(url=new_url)
			context = {
				"object":obj,
				"created":created,
			}
			if created:
				template = "shortner/success.html"
			else:
				template = "shortner/already-exists.html"
		return render(request,template,context)



class URLRedirectView(View): #class based view
	def get(self,request,shortcode = None,*args,**kwargs):
		obj = get_object_or_404(KirrURL,shortcode__iexact=shortcode)
		print(obj)
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)

