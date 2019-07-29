from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import AddNew

import random
import string

# Create your views here.
def homepage(request):
    return render(request, 'main.html', {"code": ''})

@csrf_exempt
def addNew(request):
    if request.method == 'POST':
        reqCode = request.POST['code']
        random1 = '' .join([random.choice(string.ascii_letters + string.digits) for n in range(8)])
        obj = AddNew.objects.create(code=reqCode, url=random1)
        return JsonResponse({"status": 200, "url": random1})
    return JsonResponse({"status": 400})

def view(request, id):
    try:
        obj = AddNew.objects.get(url=id)
        return render(request, 'main.html', {"code": obj.code})
    except:
        return JsonResponse({"status": 404})
   
     