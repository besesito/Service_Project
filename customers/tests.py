from django.test import TestCase
from .models import Customer

# Create your tests here.

class CustomerTestCase(TestCase):
    def setUp(self):
        self.c1 = Customer.objects.create(name="Teltonika", nip="123456546")
        self.c2 = Customer.objects.create(name="MS-Projekt", nip="987654321")
    def test_customer_intro(self):
        self.assertEqual(self.c1.natural_key(), 'Teltonika')
        self.assertEqual(self.c2.natural_key(), 'MS-Projekt')

    def test_customer_nip(self):
        self.assertEqual(self.c1.nip, "123456546")
        self.assertEqual(self.c2.nip, "987654321")

    def test_get_absolute_url(self):
        self.assertEqual(self.c1.get_absolute_url(), "/klienci/{}".format(self.c1.id))
        self.assertEqual(self.c2.get_absolute_url(), "/klienci/{}".format(self.c2.id))

 

