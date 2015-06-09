from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from django.models import Bolgs
# Create your views here.

def archive(request):
	posts = Bolgs.objects.all()
	t = loader.get_template("archive.html")
	c = Context{{'post' : posts}}
	return HttpResponse(t.render(c))