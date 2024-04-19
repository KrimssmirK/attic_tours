from django.shortcuts import render
from queues.models import Branch, Report, Service
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


def report(request, branch_id):
    logged_in_branch = Branch.objects.get(pk=branch_id)
    current_reports = Report.get_today_reports(logged_in_branch)

    services = Service.objects.all()

    context = {
        "branch_id": logged_in_branch.id,
        "branch_name": logged_in_branch.name,
        "reports": current_reports,  # dict | key: service name, value: total pax
        "services": services,
        "no_of_pax": [i for i in range(1, 101)],
        # 2x+4: where x is the branch id
        "key_shift": 4,
        "key_scale": 2,
        "today_date": timezone.now().date(),
    }
    return render(request, "queues/branch/report/container.html", context)


@csrf_exempt
def api_send_report(request):
    # inputs
    selected_service = Service.objects.get(pk=request.POST["service_id"])
    pax = request.POST["pax"]
    by = request.POST["by"]
    logged_in_branch = Branch.objects.get(pk=request.POST["branch_id"])

    # new report
    Report.objects.create(
        service=selected_service, pax=pax, by=by, branch=logged_in_branch
    )

    return JsonResponse({}, safe=False, status=200)
