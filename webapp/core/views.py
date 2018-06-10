import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ServerLog


@csrf_exempt
def create_new_node(request):
    node_data = request.GET
    ServerLog.objects.create(
        address=node_data.get('address'), port=node_data.get('port')
    )
    return JsonResponse({'success': True})