from queues.models import Branch
from django.http import JsonResponse


def get_branches(request):
    services = Branch.objects.all().values()
    return JsonResponse(list(services), safe=False, status=200)