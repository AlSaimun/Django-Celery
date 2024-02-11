from django.shortcuts import render
from .tasks import add
from celery.result import AsyncResult
# Create your views here.
from BasiCeleryProject.celery import subb
## Use delay()
def home(request):
    sub = subb.apply_async(args=[40, 2]) # method 1 add task
    result = add.delay(50, 20) # method 1 add task
    return render(request, 'myapp/home.html', {'result':result})


def check_result(request, id):
    result = AsyncResult(id)  #get task 
    print('Ready :', result.ready())
    print('Successful :', result.successful())
    print('Failed :', result.failed())
    return render(request, 'myapp/result.html', {'result':result})

