from django.shortcuts import render
from queues.models import Branch

def home(request):
    branches = Branch.objects.all().values()
    context = { "branches": list(branches) }
    return render(request, "queues/home/index.html", context=context)
