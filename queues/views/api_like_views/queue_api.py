from queues.models import Queue, Service, Branch
from django.utils import timezone
from django.http import JsonResponse


def get_queue(request, branch_id, service):
    service = Service.objects.get(name=service)
    branch = Branch.objects.get(pk=branch_id)
    print(branch)

    queue = None
    try:
        queue = Queue.objects.get(branch=branch, service=service, date__gte=timezone.now().date())
    except Queue.DoesNotExist:
        # create new queue if there is no queue set
        queue = Queue.objects.create(branch=branch, service=service)

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
    queue.window = int(str_number)
    queue.save()
    return JsonResponse({}, safe=False, status=200)


def change_call_queue(request, queue_id, switch):
    queue = Queue.objects.get(pk=queue_id)
    queue.call = True if switch == "on" else False
    queue.save()
    return JsonResponse({}, safe=False, status=200)
