from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
def index(request):

    page_title = "Jay's Dream Garage"

    stages = Stage.objects.all().order_by('sequence')

    for s in stages:
        s.cars = Car.objects.filter(stage=s)

    context = {
        'page_title': page_title,
        'stages': stages
    }

    return render(request,'kanban/index.html', context)

@csrf_exempt
def post_office(request):
    function_address = request.POST['function_address']

    if function_address == 'add_new_car':
        return add_new_car(request)
    elif function_address == 'update_car_stage':
        return update_car_stage(request)
    elif function_address == 'delete_car':
        return delete_car(request)

def delete_car(r):
    car_id = r.POST['car_id']
    Car.objects.get(id=car_id).delete()
    return JsonResponse({'stat': 'ok'})

def update_car_stage(r):
    stage_id = r.POST['stage_id']
    car_id = r.POST['car_id']

    car = Car.objects.get(id=car_id)
    car.stage_id = stage_id
    car.save()

    return JsonResponse({'stat': 'ok'})


def add_new_car(r):
    name = r.POST['name']
    car = Car.objects.create(name=name,stage_id=6)

    return JsonResponse({'car_id': car.id})
