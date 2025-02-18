from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Train
from .serializers import TrainSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class AddTrainView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Check if the user is an admin
        if request.user.role != 'admin':
            return Response({"error": "Permission denied. Only admin can add trains."}, status=status.HTTP_403_FORBIDDEN)

        # Proceed with adding the train
        serializer = TrainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainAvailabilityView(APIView):
    def get(self, request):
        source = request.query_params.get('source')
        destination = request.query_params.get('destination')
        trains = Train.objects.filter(source=source, destination=destination)
        serializer = TrainSerializer(trains, many=True)
        return Response(serializer.data)
