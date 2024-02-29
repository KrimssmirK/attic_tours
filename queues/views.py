from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# JSON
from django.http import JsonResponse, HttpResponse

from .models import Queue
from django.utils import timezone


# Views
def japan_visa_customer_queue(request):
    context = {}
    return render(request, "queues/japan_visa_queue.html", context)

def japan_visa_worker(request):
    context = {}
    return render(request, "queues/queue_worker.html", context)

# APIs
def get_japan_queue_number(request):
    current_queue_number = Queue.objects.filter(date__date=timezone.now().date())[0].current_queue_number
    data = {
        "current_queue_number": current_queue_number
    }
    return JsonResponse(data, status=200)

@csrf_exempt
def put_increase_japan_queue_number(request):
    queue = Queue.objects.filter(date__date=timezone.now().date())[0]
    queue.current_queue_number += 1
    queue.save()
    return JsonResponse({}, status=200)

@csrf_exempt
def put_decrease_japan_queue_number(request):
    queue = Queue.objects.filter(date__date=timezone.now().date())[0]
    queue.current_queue_number -= 1
    queue.save()
    return JsonResponse({}, status=200)
