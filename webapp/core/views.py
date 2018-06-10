import json
import datetime
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ServerLog


def create_new_node(request):
    node_data = request.GET
    ServerLog.objects.create(
        address=node_data.get('address'), 
        port=node_data.get('port'), 
        active=True,
    )
    return JsonResponse({'success': True})


def node_stoped(request):
    node_data = request.GET
    server = ServerLog.objects.get(
        address=node_data.get('address'), 
        port=node_data.get('port'),
    )
    server.active = False
    server.save()
    return JsonResponse({'success': True})


def log_read(request):
    node_data = request.GET
    server_log = ServerLog.objects.filter(
        address=node_data.get('address'), 
        port=node_data.get('port'),
    ).latest('created')
    server_log.read_amount += 1
    server_log.save()
    return JsonResponse({'success': True})


def log_write(request):
    node_data = request.GET
    server_log = ServerLog.objects.filter(
        address=node_data.get('address'), 
        port=node_data.get('port'),
    ).latest('created')
    server_log.write_amount += 1
    server_log.save()
    return JsonResponse({'success': True})


def servers_list(request):
    servers_list = ServerLog.objects.all().order_by('-created')
    cluster_capacity = 15
    intervals = [datetime.datetime.now() - datetime.timedelta(minutes=m) for m in reversed(range(1, 5))]
    num_of_active_servers = [ServerLog.objects.filter(active=True, created__lte=i).count() for i in intervals]
    intervals = [i.time() for i in intervals]
    utilization = [(num_s / cluster_capacity) * 100 for num_s in num_of_active_servers]
    context = {
        'servers_list': servers_list,
        'num_of_active_servers': num_of_active_servers,
        'intervals': [str(i) for i in intervals],
        'utilization': utilization,
    }
    return render(request, 'core/servers_list.html', context)


def server_info(request, pk):
    server = ServerLog.objects.get(pk=pk)
    max_read_capacity = 5000
    max_write_capacity = 5000
    intervals = [datetime.datetime.now()]
    intervals = [i.time() for i in intervals]
    read_data = server.read_amount / max_read_capacity
    active_time = datetime.datetime.now(datetime.timezone.utc) - server.created
    context = {
        'server': server,
        'intervals': [str(i) for i in intervals],
        'requests_processed': server.read_amount + server.write_amount,
        'active_time': str(active_time),
    }
    return render(request, 'core/server.html', context)
