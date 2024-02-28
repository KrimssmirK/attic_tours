from django.shortcuts import render

# JSON
from django.http import JsonResponse

from .models import Queue
from django.utils import timezone

# Create your views here.

def japan_queue_view_customer(request):
    context = {}
    return render(request, "queues/japan_visa_queue.html", context)

# APIs
def get_japan_queue_number(request):
    current_number = Queue.objects.filter(date__date=timezone.now().date())[0].current_number
    data = {
        "current_number": current_number
    }
    return JsonResponse(data, status=200)

def japan_queue_view_worker(request):
    context = {}
    return render(request, "queues/queue_worker.html", context)