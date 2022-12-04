from django.test import TestCase, Client
from shop.models import Product, Purchase
from shop.queries import product_data
from urllib.parse import urlencode


class PurchaseCreateTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        test1 = Product.objects.create(
            name='test1', price='500', initial_amount='10')

        self.request_url = f'/buy/{test1.id}/'
        self.request_data = urlencode({
            'product': test1.id,
            'person': 'test_person',
            'address': 'test_address',
        })

    def tearDown(self):
        Product.objects.all().delete()
        Purchase.objects.all().delete()

    def _post_form(self):
        """Отправить запрос на покупку одного предмета"""

        return self.client.post(
            self.request_url,
            self.request_data,
            content_type="application/x-www-form-urlencoded",
        )

    def _post_repeat(self, times=2):
        """Повторить запрос times раз"""

        for _ in range(times):
            self._post_form()

    def test_can_post(self):
        """Форма работает и принимает post"""

        response = self._post_form()
        self.assertEquals(response.status_code, 200)

    def test_created(self):
        """Форма создаёт объекты Purchase"""

        self._post_form()
        self.assertEquals(Purchase.objects.count(), 1)

    def test_amount_decrease(self):
        """Количество товаров уменьшается"""

        self._post_form()
        product = Product.objects.raw(product_data)[0]
        self.assertEquals(product.amount_left, 9)

    def test_price_increase(self):
        """Цена увеличивается при уменьшении количества более чем в 2 раза"""

        self._post_repeat(6)

        product = Product.objects.raw(product_data)[0]

        self.assertEquals(product.amount_left, 4)
        self.assertEquals(product.price, 600)

    def test_sold_out(self):
        """Если не осталось товара, то отображается 'Нет в наличии'"""

        self._post_repeat(10)

        response = self.client.get('/')
        self.assertTrue('Нет в наличии' in response.content.decode())
