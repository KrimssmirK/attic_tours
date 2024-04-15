from django.shortcuts import render
from branch.models import Branch
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate, login


def branch_select(request):
    branches = Branch.objects.all().values()
    context = {
        "branches": list(branches)
    }
    return render(request, "branch/index.html", context)


@csrf_exempt
def login_branch(request):
    username = request.POST["username"]
    password = request.POST["password"]
    print("username:", username)
    print("password:", password)
    SUCCESS = False
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        SUCCESS = True
    result = {
        "success": SUCCESS
    }
    return JsonResponse(result, safe=False, status=200)