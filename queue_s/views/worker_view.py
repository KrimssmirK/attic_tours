from django.shortcuts import render
from branch.models import Branch


def worker_queue(request, branch_id):
    selected_branch = Branch.objects.get(pk=branch_id)
    context = {
        "branch_id": selected_branch.id,
        "branch_name": selected_branch.name
    }
    return render(request, "queues/worker_queue.html", context)