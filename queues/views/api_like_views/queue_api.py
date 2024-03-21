# get the current queue
from queues.models import Queue, Service
from django.utils import timezone
from django.http import JsonResponse
from django.http import HttpResponse


def get_queue(request, service):
    service = Service.objects.get(name=service)
    
    queue = None
    try:
        queue = Queue.objects.get(service=service, date__lte=timezone.now().date())
    except Queue.DoesNotExist:
        # create new queue if there is no queue set
        queue = Queue.objects.create(service=service)
    
    # this is the format to communicate with the front-end
    data = queue.convert_attrbs_to_dict()
    
    return JsonResponse(data, safe=False, status=200)


def change_number_queue(request, queue_id, str_number):
    queue = Queue.objects.get(pk=queue_id)
    queue.number += int(str_number)
    queue.save()
    return JsonResponse({}, safe=False, status=200)


def change_window_queue(request, queue_id, str_number):
    queue = Queue.objects.get(pk=queue_id)
    queue.window += int(str_number)
    queue.save()
    return JsonResponse({}, safe=False, status=200)


def change_call_queue(request, queue_id, switch):
    queue = Queue.objects.get(pk=queue_id)
    queue.call = True if switch == "on" else False
    queue.save()
    return JsonResponse({}, safe=False, status=200)