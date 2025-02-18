from django.urls import path
from .views import BookSeatView, BookingDetailView

urlpatterns = [
    path('book/', BookSeatView.as_view(), name="book_seat"),
    path('detail/<int:booking_id>/', BookingDetailView.as_view(), name="booking_detail"),
]
