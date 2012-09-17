# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from cardviewer.models import Card

def home (request):
  return render(request, "home.html", {})
  #return HttpResponse("die in a fire")
  
def detail(request, card_id):
  card = get_object_or_404(Card, id=card_id)
  return render(request, "detail.html", {'theCard':card})
 #return HttpResponse("You're looking at card %s." % card_id)

def home(request):
  return render(request, "home.html", {})
 #return HttpResponse("You're looking at the home page!")

