from django.views import View
from django.http import HttpRequest, HttpResponse


class ItemsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('GET request')

    def post(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('POST request')

    def delete(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('DELETE request')

    def put(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse('PUT request')
