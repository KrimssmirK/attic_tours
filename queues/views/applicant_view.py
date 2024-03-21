from django.shortcuts import render


def applicant_queue(request):
    context = {}
    return render(request, "queues/new_customer_queue.html", context)