from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# JSON
from django.http import JsonResponse
import json

from .models import JapanQueue, KoreaTicketQueue, Window
from django.utils import timezone


# Views
def queue(request):
    context = {}
    return render(request, "queues/new_queue.html", context)


def customer_queue(request):
    context = {}
    return render(request, "queues/new_customer_queue.html", context)




# APIs
def get_japan_korea_ticket_queue(request):
    
    
    current_japan_queues = JapanQueue.objects.filter(date__date=timezone.now())
    current_korea_ticket_queues = KoreaTicketQueue.objects.filter(date__date=timezone.now())

    if len(list(current_japan_queues)) == 0:    
        window_1 = Window.objects.create()
        japan_queue_0 = JapanQueue.objects.create(window=window_1)
        current_japan_queue = japan_queue_0
    else:
        current_japan_queue = current_japan_queues[0]
        
    if len(list(current_korea_ticket_queues)) == 0:    
        window_1 = Window.objects.get(pk=1)
        korea_ticket_queue_0 = KoreaTicketQueue.objects.create(window=window_1)
        current_korea_ticket_queue = korea_ticket_queue_0
    else:
        current_korea_ticket_queue = current_korea_ticket_queues[0]
        
    
    
    current_japan_queue_window = Window.objects.get(pk=current_japan_queue.window_id)
    current_korea_ticket_queue_window = Window.objects.get(pk=current_korea_ticket_queue.window_id)
    windows = Window.objects.all()

    data = {
        "current_japan_queue": {
            "number": current_japan_queue.number,
            "call": current_japan_queue.call
            },
        "current_korea_ticket_queue": {
            "number": current_korea_ticket_queue.number,
            "call": current_korea_ticket_queue.call
        },
        "current_japan_queue_window": {
            "number": current_japan_queue_window.number,
            "service_type": current_japan_queue_window.service_type
            },
        "current_korea_ticket_queue_window": {
            "number": current_korea_ticket_queue_window.number,
            "service_type": current_korea_ticket_queue_window.service_type
            },
        "windows": list(windows.values())
    }
    
    # reset call
    current_japan_queue.call = False
    current_japan_queue.save()
    current_korea_ticket_queue.call = False
    current_korea_ticket_queue.save()
    
    return JsonResponse(data, safe=False, status=200)


@csrf_exempt
def put_increase_japan_queue_number(request):
    received_data = json.loads(request.body)
    queue = JapanQueue.objects.filter(date__date=timezone.now())[0]
    queue.number += 1
    queue.window = Window.objects.get(pk=int(received_data['window_id']))
    queue.save()
    return JsonResponse({}, status=200)

@csrf_exempt
def put_decrease_japan_queue_number(request):
    received_data = json.loads(request.body)
    queue = JapanQueue.objects.filter(date__date=timezone.now())[0]
    if (queue.number != 0):
        queue.number -= 1
        queue.window = Window.objects.get(pk=int(received_data['window_id']))
        queue.save()
    return JsonResponse({}, status=200)


@csrf_exempt
def call_japan_applicant(request):
    queue = JapanQueue.objects.filter(date__date=timezone.now())[0]
    queue.call = True
    queue.save()
    return JsonResponse({}, status=200)


@csrf_exempt
def set_japan_window(request):
    received_data = json.loads(request.body)
    queue = JapanQueue.objects.filter(date__date=timezone.now())[0]
    queue.window = Window.objects.get(pk=int(received_data['window_id']))
    queue.save()
    return JsonResponse({}, status=200)

@csrf_exempt
def put_increase_korea_ticket_queue_number(request):
    received_data = json.loads(request.body)
    queue = KoreaTicketQueue.objects.filter(date__date=timezone.now())[0]
    queue.number += 1
    queue.window = Window.objects.get(pk=int(received_data['window_id']))
    queue.save()
    return JsonResponse({}, status=200)

@csrf_exempt
def put_decrease_korea_ticket_queue_number(request):
    received_data = json.loads(request.body)
    queue = KoreaTicketQueue.objects.filter(date__date=timezone.now())[0]
    if (queue.number != 0):
        queue.number -= 1
        queue.window = Window.objects.get(pk=int(received_data['window_id']))
        queue.save()
    return JsonResponse({}, status=200)


@csrf_exempt
def call_korea_ticket_applicant(request):
    queue = KoreaTicketQueue.objects.filter(date__date=timezone.now())[0]
    queue.call = True
    queue.save()
    return JsonResponse({}, status=200)


@csrf_exempt
def set_korea_ticket_window(request):
    received_data = json.loads(request.body)
    queue = KoreaTicketQueue.objects.filter(date__date=timezone.now())[0]
    queue.window = Window.objects.get(pk=int(received_data['window_id']))
    queue.save()
    return JsonResponse({}, status=200)