from rest_framework.response import Response
from users.api.serializers.user_serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

class UserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)