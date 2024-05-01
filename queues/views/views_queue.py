from django.shortcuts import render
from queues.models import Branch, Service, PrefQueue
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # for enabling post request


def queue(request, branch_id):
    logged_in_branch = Branch.objects.get(pk=branch_id)
    return render(
        request,
        "queues/branch/queue/container.html",
        {
            "branch_id": branch_id,
            "branch_name": logged_in_branch.name,
            "key_shift": 4,
            "key_scale": 2,
        },
    )


def api_get_services(request):
    services = Service.objects.all().values()
    return JsonResponse(
        {
            "services": list(services),
        },
        safe=False,
        status=200,
    )


def api_get_pref_queues(request):
    branch = Branch.objects.get(id=request.GET["branch_id"])
    pref_queues = PrefQueue.objects.filter(branch=branch).values()
    return JsonResponse(
        {
            "pref_queues": list(pref_queues),
        },
        safe=False,
        status=200,
    )


@csrf_exempt
def api_create_pref_queue(request):
    """add preference queue per branch"""
    status = ""
    branch = Branch.objects.get(id=request.POST["branch_id"])
    service = Service.objects.get(id=request.POST["service_id"])
    pref_queues = PrefQueue.objects.filter(branch=branch, service=service)
    if not pref_queues.exists():
        PrefQueue.objects.create(branch=branch, service=service)
        status = "new service has been added to preference queue"
    else:
        status = "has already in preference queue"
    # if pref_queues empty then create pref_queue
    # if not empty then do nothing

    return JsonResponse(data={"status": status})
