from django.contrib.auth.decorators import login_not_required
from django.shortcuts import render


# Create your views here.

@login_not_required
def home(request):
    return render(request, 'base/home.html')
