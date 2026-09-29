from django.views import View
from django.http import HttpRequest, HttpResponse


def items_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return HttpResponse('GET request')
    elif request.method == 'POST':
        return HttpResponse('POST request')
    elif request.method == 'DELETE':
        return HttpResponse('DELETE request')
    elif request.method == 'PUT':
        return HttpResponse('PUT request')
    else:
        return HttpResponse('page not found')
