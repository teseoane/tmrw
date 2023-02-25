import datetime

from django.http import JsonResponse


def status_view(request):
    return JsonResponse(
        {
            'status': 'OK',
            'timestamp': datetime.datetime.now().timestamp(),
        }
    )
