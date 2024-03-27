from django.shortcuts import render
from branch.models import Branch


def branch_select(request):
    branches = Branch.objects.all().values()
    context = {
        "branches": list(branches)
    }
    return render(request, "branch/index.html", context)