from django.shortcuts import render


def worker_queue(request):
    context = {}
    return render(request, "queues/new_worker.html", context)