from django.test import TestCase
from restaurant.models import menu
from restaurant.serializers import menuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = menu.objects.create(Title="Pizza", Price=9.99, Inventory=10)
        self.item2 = menu.objects.create(Title="Burger", Price=5.49, Inventory=20)
        self.item3 = menu.objects.create(Title="Pasta", Price=7.25, Inventory=15)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))  # uses the name='menu-list' from urls
        menu_items = menu.objects.all()
        serializer = menuSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)