from django.test import TestCase
from base.models import Product, Ingredient, ProductIngredient


class OrderTestCase(TestCase):

    def setUp(self):
        self.beef = Ingredient.objects.create(
            name="Beef", stock=20000, initial_stock=20000
        )
        self.cheese = Ingredient.objects.create(
            name="Cheese", stock=5000, initial_stock=5000
        )
        self.onion = Ingredient.objects.create(
            name="Onion", stock=1000, initial_stock=1000
        )

        self.burger = Product.objects.create(name="Burger")
        ProductIngredient.objects.create(
            product=self.burger, ingredient=self.beef, amount=150
        )
        ProductIngredient.objects.create(
            product=self.burger, ingredient=self.cheese, amount=30
        )
        ProductIngredient.objects.create(
            product=self.burger, ingredient=self.onion, amount=20
        )

    def test_order_creation_and_stock_update(self):
        response = self.client.post(
            "/api/v1/order/",
            {"products": [{"product_id": self.burger.id, "quantity": 2}]},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)

        self.beef.refresh_from_db()
        self.cheese.refresh_from_db()
        self.onion.refresh_from_db()

        self.assertEqual(self.beef.stock, 19700)
        self.assertEqual(self.cheese.stock, 4940)
        self.assertEqual(self.onion.stock, 960)

    def test_low_stock_email_triggered(self):
        response = self.client.post(
            "/api/v1/order/",
            {"products": [{"product_id": self.burger.id, "quantity": 100}]},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)

        self.beef.refresh_from_db()
        self.cheese.refresh_from_db()
        self.onion.refresh_from_db()

        self.assertTrue(self.beef.low_stock_alert_sent)
        self.assertTrue(self.cheese.low_stock_alert_sent)
        self.assertTrue(self.onion.low_stock_alert_sent)
