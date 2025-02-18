from django.urls import path
from .views import AddTrainView, TrainAvailabilityView

urlpatterns = [
    path('add/', AddTrainView.as_view(), name="add_train"),
    path('availability/', TrainAvailabilityView.as_view(), name="train_availability"),
]
