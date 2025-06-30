import pytest
from django.urls import reverse
from django.test import Client
from products.models import Product

@pytest.fixture
def product():
    return Product.objects.create(name="Test Product", description="Test Description", price=9.99)

@pytest.mark.django_db
def test_product_list_view(client):
    url = reverse('product_list')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_product_detail_view(client, product):
    url = reverse('product_detail', args=[product.pk])
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_product_create_view(client):
    url = reverse('product_create')
    data = {
        'name': 'New Product',
        'description': 'New Description',
        'price': 19.99
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Product.objects.filter(name='New Product').exists()

@pytest.mark.django_db
def test_product_update_view(client, product):
    url = reverse('product_update', args=[product.pk])
    data = {
        'name': 'Updated Product',
        'description': 'Updated Description',
        'price': 29.99
    }
    response = client.post(url, data)
    assert response.status_code == 302
    product.refresh_from_db()
    assert product.name == 'Updated Product'

@pytest.mark.django_db
def test_product_delete_view(client, product):
    url = reverse('product_delete', args=[product.pk])
    response = client.post(url)
    assert response.status_code == 302
    assert not Product.objects.filter(pk=product.pk).exists()