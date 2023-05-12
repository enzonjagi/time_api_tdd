from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

def time_api(request):
    """Written for the sake of passing tests"""

    return JsonResponse({
        'current_time': datetime.now().strftime(settings.DATETIME_FORMAT)
    })
