from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from ..serializers import UserCreateSerializer


class ItemsView(APIView):
    def get(self, request: Request) -> Response:
        search = request.query_params.get('search')
        limit = request.query_params.get('limit')

        print(search, limit)

        return Response({'message': 'GET request'})

    def post(self, request: Request) -> Response:
        data = request.data
        print(data)

        return Response({'message': 'POST request'})

    def delete(self, request: Request) -> Response:
        return Response({'message': 'DELETE request'})

    def put(self, request: Request) -> Response:
        return Response({'message': 'PUT request'})


class UserCreateView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.validated_data)

