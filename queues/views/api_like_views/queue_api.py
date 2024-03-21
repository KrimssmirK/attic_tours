# get the current queue
from queues.models import Queue, Service
from django.utils import timezone
from django.http import JsonResponse
from django.http import HttpResponse


def get_queue(request):
    service_name = "Japan Visa" # CONSTANT -> DYNAMIC
    service = Service.objects.get(name=service_name)
    
    queue = None
    try:
        queue = Queue.objects.get(service=service, date__lte=timezone.now().date())
    except Queue.DoesNotExist:
        queue = Queue.objects.create(service=service)
    
    data = {
        "test": 1
    }
    
    return HttpResponse(data.test)
    # return JsonResponse(data, safe=False, status=200)