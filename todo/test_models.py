from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defualts_to_false(self):
        item = Item.objects.create(name='TEst Todo Item')
        self.assertFalse(item.done)
