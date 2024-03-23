from queues.models import Service
from django.http import JsonResponse


def get_services(request):
    services = Service.objects.all().values()
    return JsonResponse(list(services), safe=False, status=200)