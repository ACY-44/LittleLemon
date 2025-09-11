from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from .serializers import menuSerializer, bookingSerializer
from .models import menu, booking
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer

