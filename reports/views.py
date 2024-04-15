from django.shortcuts import render
from reports.models import Report, ReportType
from branch.models import Branch
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def report(request, branch_id):
    
    selected_branch = Branch.objects.get(pk=branch_id)
    reports = Report.get_current_reports(selected_branch)

    report_types = ReportType.objects.all()

    context = {
        "branch_id": selected_branch.id,
        "branch_name": selected_branch.name,
        "reports": reports,
        "report_types": report_types,
        "no_of_pax": [i for i in range(1, 101)]
    }

    return render(request, "reports/stats.html", context)


@csrf_exempt
def api_send_report(request):
    # inputs
    branch_id = request.POST["branch_id"]
    selected_branch = Branch.objects.get(pk=branch_id)
    report_type_id = request.POST["report_type_id"]
    selected_report_type = ReportType.objects.get(pk=report_type_id)
    entered_coordinator = request.POST["coordinator"]
    no_of_pax = request.POST["no_of_pax"]
    
    # new report
    Report.objects.create(
        branch=selected_branch,
        report_type=selected_report_type,
        coordinator=entered_coordinator,
        no_of_pax=no_of_pax
    )
    
    return JsonResponse({}, safe=False, status=200)
