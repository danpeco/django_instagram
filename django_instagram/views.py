# Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json


def hello(request):
    '''Return a greeting'''
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'hello my friend, current server time is {now}')

def sort_numbers(request):
    '''Return a JSON response with sorted integers'''
    # import pdb; pdb.set_trace()
    numbers = [int(i) for i in sorted(request.GET['numbers'].split(','))]
    sorted_numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Numbers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4),
                        content_type='application/json')


def welcome(request, name, age):
    '''Checks age and return a greeting if age > 12 or denise otherwise'''
    if age < 12:
        return HttpResponse(f'Sorry {name}, you must be older than 12 years to login')
    else:
        return HttpResponse(f'Hello {name}, Welcome to instagram')

