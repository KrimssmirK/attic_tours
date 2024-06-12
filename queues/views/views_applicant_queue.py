from django.shortcuts import render
from queues.models import Branch


def applicant_queue(request, branch_id):
    logged_in_branch = Branch.objects.get(pk=branch_id)
    if logged_in_branch.name == "MAIN OFFICE":
        return render(
            request,
            "queues/applicant/applicant_view_main.html",
            {
                "branch_id": branch_id,
                # "branch_name": logged_in_branch.name,
                # "key_shift": 4,
                # "key_scale": 2,
            },
        )
    else:
        return render(
            request,
            "queues/applicant/applicant_view.html",
            {
                "branch_id": branch_id,
                # "branch_name": logged_in_branch.name,
                # "key_shift": 4,
                # "key_scale": 2,
            },
        )
