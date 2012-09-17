# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def home (request):
  return render(request, "home.html", {})
  #return HttpResponse("die in a fire")
  
def detail(request, card_id):
  return HttpResponse("You're looking at card %s." % card_id)
 #return render(request, "detail.html", {})
