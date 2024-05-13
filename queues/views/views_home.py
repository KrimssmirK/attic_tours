from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from queues.models import Branch

def home(request):
    branches = Branch.get_branch_without_password()
    context = { "branches": branches }
    return render(request, "queues/home/index.html", context=context)


@csrf_exempt
def login(request):
    # access token f(x) I invented
    # f(x) such that x is the branchId
    # f(x) = 2x + 4
    def generate_access_token(branchId):
        return 2 * int(branchId) + 4
    
    branchId = request.POST["branchId"]
    password = request.POST["password"]
    branch = Branch.objects.get(id=branchId)
    if password == branch.password:
        password_matched = True
    else: 
        password_matched = False 
    return JsonResponse(
        {
            "password_matched": password_matched,
            "access_token": generate_access_token(branchId) if password_matched else None
        }, 
        safe=False
    )
