from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class PingApiView(APIView):
    """
    This is an example Ping API View for DRF
    """

    def get(self, request: Request) -> Response:
        return Response({"message": "pong!"})

    def post(self, request: Request) -> Response:
        return Response(
            data={
                "message": "Created pong!",
                "post-data": request.data,
            },
            status=status.HTTP_201_CREATED,
        )

    def patch(self, request: Request) -> Response:
        return Response({"message": "Updated pong!"})

    def delete(self, request: Request) -> Response:
        return Response({"message": "Deleted pong!"})
