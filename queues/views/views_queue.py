from django.shortcuts import render
from queues.models import Branch, Service
from django.http import JsonResponse


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
    return JsonResponse({
        "services": list(services),
        }, safe=False, status=200)
