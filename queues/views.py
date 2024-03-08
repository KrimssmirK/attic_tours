from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# JSON
from django.http import JsonResponse
import json

from .models import Queue, Window
from django.utils import timezone


# Views
def queue(request):
    context = {}
    return render(request, "queues/new_queue.html", context)


def customer_queue(request):
    context = {}
    return render(request, "queues/new_customer_queue.html", context)




# APIs
def get_japan_queue(request):
    
    
    current_queues = Queue.objects.filter(date__date=timezone.now())

    if len(list(current_queues)) == 0:    
        window_1 = Window.objects.create()
        queue_0 = Queue.objects.create(window=window_1)
        current_queue = queue_0
    else:
        current_queue = current_queues[0]
        
    
    
    current_window = Window.objects.get(pk=current_queue.window_id)
    windows = Window.objects.all()

    data = {
        "current_queue": {
            "number": current_queue.current_queue_number,
            "call": current_queue.call
            },
        "current_window": {
            "number": current_window.number,
            "service_type": current_window.service_type
            },
        "windows": list(windows.values())
    }
    
    # reset call
    current_queue.call = False
    current_queue.save()
    
    return JsonResponse(data, safe=False, status=200)


@csrf_exempt
def put_increase_japan_queue_number(request):
    received_data = json.loads(request.body)
    queue = Queue.objects.filter(date__date=timezone.now())[0]
    queue.current_queue_number += 1
    queue.window = Window.objects.get(pk=int(received_data['window_id']))
    queue.save()
    return JsonResponse({}, status=200)

@csrf_exempt
def put_decrease_japan_queue_number(request):
    received_data = json.loads(request.body)
    queue = Queue.objects.filter(date__date=timezone.now())[0]
    if (queue.current_queue_number != 0):
        queue.current_queue_number -= 1
        queue.window = Window.objects.get(pk=int(received_data['window_id']))
        queue.save()
    return JsonResponse({}, status=200)


@csrf_exempt
def call_applicant(request):
    queue = Queue.objects.filter(date__date=timezone.now())[0]
    queue.call = True
    queue.save()
    return JsonResponse({}, status=200)


@csrf_exempt
def set_window(request):
    received_data = json.loads(request.body)
    queue = Queue.objects.filter(date__date=timezone.now())[0]
    queue.window = Window.objects.get(pk=int(received_data['window_id']))
    queue.save()
    return JsonResponse({}, status=200)