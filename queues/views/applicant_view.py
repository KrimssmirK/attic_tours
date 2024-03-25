from django.shortcuts import render
from queues.models import Branch


def applicant_queue(request, branch_name):
    print("branch_name from views:", branch_name)
    target_branch = Branch.objects.get(name=branch_name)
    context = {
        "branch_id": target_branch.id,
        "branch_name": target_branch.name,
        "branch_mobile_no": target_branch.mobile_no,
        "branch_landline_no": target_branch.landline_no
    }
    return render(request, "queues/applicant_queue.html", context)