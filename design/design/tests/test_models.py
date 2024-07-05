from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

from main.models import Rate, Price, Service

class IntegrationTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.rate = Rate.objects.create(title="Test Rate")

    def test_get_rate(self):
        response = self.client.get(reverse('rate-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], self.rate.title)

    def test_create_price(self):
        response = self.client.post(reverse('price-list'), {
            'price': '100',
            'description': 'Test Description',
            'rate': self.rate.id
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['price'], '100')
        self.assertEqual(response.data['description'], 'Test Description')
        self.assertEqual(response.data['rate'], self.rate.id)

    def test_get_price(self):
        price = Price.objects.create(price='100', description='Test Description', rate=self.rate)
        response = self.client.get(reverse('price-detail', args=[price.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['price'], price.price)
        self.assertEqual(response.data['description'], price.description)
        self.assertEqual(response.data['rate'], self.rate.id)

    def test_create_service(self):
        response = self.client.post(reverse('service-list'), {
            'title': 'Test Service',
            'rate': self.rate.id
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Service')
        self.assertEqual(response.data['rate'], self.rate.id)

    def test_get_service(self):
        service = Service.objects.create(title='Test Service', rate=self.rate)
        response = self.client.get(reverse('service-detail', args=[service.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], service.title)
        self.assertEqual(response.data['rate'], self.rate.id)
