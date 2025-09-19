from django.test import TestCase
from restaurant.models import menu

class TestMenu(TestCase):
    def test_get_item(self):
        item = menu.objects.create(Title="Pizza", Price=9.99, Inventory=10)
        self.assertEqual(str(item), "Pizza : 9.99")