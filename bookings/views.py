from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db import transaction
from .models import Booking
from trains.models import Train
from .serializers import BookingSerializer

class BookSeatView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        train_id = request.data.get("train_id")

        try:
            with transaction.atomic():
                train = Train.objects.select_for_update().get(id=train_id)

                if train.available_seats > 0:
                    seat_number = train.total_seats - train.available_seats + 1
                    train.available_seats -= 1
                    train.save()

                    booking = Booking.objects.create(user=request.user, train=train, seat_number=seat_number)

                    return Response({
                        "message": "Booking successful",
                        "booking_id": booking.id,
                        "seat_number": seat_number
                    }, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "No seats available"}, status=status.HTTP_400_BAD_REQUEST)

        except Train.DoesNotExist:
            return Response({"error": "Train not found"}, status=status.HTTP_404_NOT_FOUND)

class BookingDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id, user=request.user)
            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)
