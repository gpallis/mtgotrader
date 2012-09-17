# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def collection(request):
    return HttpResponse("Cards don't exist yet, silly!")