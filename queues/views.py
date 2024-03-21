from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models.query import EmptyQuerySet
from django.http import JsonResponse
import json
from .models import Service, Queue
from django.utils import timezone


# Views
def queue(request):
    context = {}
    return render(request, "queues/new_worker.html", context)


def customer_queue(request):
    context = {}
    return render(request, "queues/new_customer_queue.html", context)



def set_current_queue_number(model):
    pass


# helper functions
def get_current_queue_number(model):
    current_queue = model.objects.filter(date__date=timezone.now())
    # what if empty?
    if current_queue is EmptyQuerySet:
        pass
    return current_queue
    
    

# like APIs
def get_japan_korea_ticket_queue(request):
    # flow
    # 1. get the current japan visa queue number
    # 2. get the current korea visa queue number
    # 3. send the data
    
    

    data = {
        "current_japan_queue": {
            "number": 0,
            "call": False
            },
        "current_korea_ticket_queue": {
            "number": 0,
            "call": False
        },
        "current_japan_queue_window": {
            "number": 0,
            "service_type": ""
            },
        "current_korea_ticket_queue_window": {
            "number": 0,
            "service_type": "urrent_korea_ticket_queue_window.service_type"
            },
        "windows": []
    }
    
    # reset call
  
    
    return JsonResponse(data, safe=False, status=200)


@csrf_exempt
def put_increase_japan_queue_number(request):
    # received_data = json.loads(request.body)
    # queue = JapanQueue.objects.filter(date__date=timezone.now())[0]
    # queue.number += 1
    # queue.window = Window.objects.get(pk=int(received_data['window_id']))
    # queue.save()
    return JsonResponse({}, status=200)

@csrf_exempt
def put_decrease_japan_queue_number(request):
    # received_data = json.loads(request.body)
    # queue = JapanQueue.objects.filter(date__date=timezone.now())[0]
    # if (queue.number != 0):
    #     queue.number -= 1
    #     queue.window = Window.objects.get(pk=int(received_data['window_id']))
    #     queue.save()
    return JsonResponse({}, status=200)


@csrf_exempt
def call_japan_applicant(request):
    # queue = JapanQueue.objects.filter(date__date=timezone.now())[0]
    # queue.call = True
    # queue.save()
    return JsonResponse({}, status=200)


@csrf_exempt
def set_japan_window(request):
    # received_data = json.loads(request.body)
    # queue = JapanQueue.objects.filter(date__date=timezone.now())[0]
    # queue.window = Window.objects.get(pk=int(received_data['window_id']))
    # queue.save()
    return JsonResponse({}, status=200)

@csrf_exempt
def put_increase_korea_ticket_queue_number(request):
    # received_data = json.loads(request.body)
    # queue = KoreaTicketQueue.objects.filter(date__date=timezone.now())[0]
    # queue.number += 1
    # queue.window = Window.objects.get(pk=int(received_data['window_id']))
    # queue.save()
    return JsonResponse({}, status=200)

@csrf_exempt
def put_decrease_korea_ticket_queue_number(request):
    # received_data = json.loads(request.body)
    # queue = KoreaTicketQueue.objects.filter(date__date=timezone.now())[0]
    # if (queue.number != 0):
    #     queue.number -= 1
    #     queue.window = Window.objects.get(pk=int(received_data['window_id']))
    #     queue.save()
    return JsonResponse({}, status=200)


@csrf_exempt
def call_korea_ticket_applicant(request):
    # queue = KoreaTicketQueue.objects.filter(date__date=timezone.now())[0]
    # queue.call = True
    # queue.save()
    return JsonResponse({}, status=200)


@csrf_exempt
def set_korea_ticket_window(request):
    # received_data = json.loads(request.body)
    # queue = KoreaTicketQueue.objects.filter(date__date=timezone.now())[0]
    # queue.window = Window.objects.get(pk=int(received_data['window_id']))
    # queue.save()
    return JsonResponse({}, status=200)