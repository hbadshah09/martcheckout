import unittest
from checkout import Product, Discount, Checkout

class TestCheckout(unittest.TestCase):

    def setUp(self):
        products = [
            Product('A', 50),
            Product('B', 30),
            Product('C', 20),
            Product('D', 15),
            Product('E', 40),
            Product('F', 10),
            Product('G', 25)
        ]
        discounts = [
            Discount('A', 3, 130),
            Discount('B', 2, 45),
            Discount('E', 4, 150),
            Discount('F', 5, 45)
        ]
        self.checkout = Checkout(products, discounts)

    def test_empty_cart(self):
        self.assertEqual(self.checkout.calculate_total(), 0)

    def test_single_item(self):
        self.checkout.scan('A')
        self.assertEqual(self.checkout.calculate_total(), 50)

    def test_multiple_items(self):
        items = "CDBA"
        for item in items:
            self.checkout.scan(item)
        self.assertEqual(self.checkout.calculate_total(), 115)

    def test_discounted_items(self):
        items = "AAA"
        for item in items:
            self.checkout.scan(item)
        self.assertEqual(self.checkout.calculate_total(), 130)

    def test_mixed_items_with_discount(self):
        items = "AAABB"
        for item in items:
            self.checkout.scan(item)
        self.assertEqual(self.checkout.calculate_total(), 175)

    def test_mixed_items_without_discount(self):
        items = "DABABA"
        for item in items:
            self.checkout.scan(item)
        self.assertEqual(self.checkout.calculate_total(), 190)

    def test_new_discount_items(self):
        items = "EEEE"
        for item in items:
            self.checkout.scan(item)
        self.assertEqual(self.checkout.calculate_total(), 150)

    def test_mixed_new_items(self):
        items = "EFFGG"
        for item in items:
            self.checkout.scan(item)
        self.assertEqual(self.checkout.calculate_total(), 90)

if __name__ == "__main__":
    unittest.main()
