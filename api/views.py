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


class ItemsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('GET request')

    def post(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('POST request')

    def delete(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('DELETE request')

    def put(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('PUT request')
