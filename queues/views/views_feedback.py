from django.shortcuts import render
from queues.models import Branch


def feedback(request, branch_id):
    logged_in_branch = Branch.objects.get(pk=branch_id)
    return render(
        request,
        "queues/branch/feedback/container.html",
        {
            "branch_id": branch_id,
            "branch_name": logged_in_branch.name,
            "key_shift": 4,
            "key_scale": 2,
        },
    )
