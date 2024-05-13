from django.shortcuts import render
from queues.models import Branch, Feedback
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def api_send_feedback(request):
    feedback = Feedback(
        title=request.POST["title"],
        description=request.POST["description"],
        branch_id=request.POST["branch_id"],
    )
    feedback.save()
    return JsonResponse(
        data={"status": f"{feedback} has been created and saved!"},
        safe=False,
        status=201,
    )
