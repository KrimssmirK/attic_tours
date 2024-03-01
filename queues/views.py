from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# JSON
from django.http import JsonResponse

from .models import Queue
from django.utils import timezone


# Views
def queue(request):
    context = {}
    return render(request, "queues/queue.html", context)


def customer_queue(request):
    context = {}
    return render(request, "queues/customer_queue.html", context)



# APIs
def get_japan_queue_number(request):
    try:
        current_queue_number = Queue.objects.filter(date__date=timezone.now().date())[0].current_queue_number
    except Exception:
        current_queue_number = 0
    data = {
        "current_queue_number": current_queue_number
    }
    return JsonResponse(data, status=200)

@csrf_exempt
def put_increase_japan_queue_number(request):
    try:
        queue = Queue.objects.filter(date__date=timezone.now().date())[0]
    except Exception:
        Queue().save()
        queue = Queue.objects.filter(date__date=timezone.now().date())[0]
    
    queue.current_queue_number += 1
    queue.save()
    return JsonResponse({}, status=200)

@csrf_exempt
def put_decrease_japan_queue_number(request):
    try:
        queue = Queue.objects.filter(date__date=timezone.now().date())[0]
    except Exception:
        Queue().save()
        queue = Queue.objects.filter(date__date=timezone.now().date())[0]
    if (queue.current_queue_number != 0):
        queue.current_queue_number -= 1
        queue.save()
    return JsonResponse({}, status=200)
