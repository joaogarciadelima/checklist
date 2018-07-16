from os import path

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from checklistos.django_assertions import dj_assert_contains
from checklistos.produtos.models import Produto


# def test_app_link_in_home(client):
#     response = client.get('/')
#     dj_assert_contains(response, reverse('servicos:index'))


IMAGE_PATH = path.dirname(__file__)
IMAGE_PATH = path.join(IMAGE_PATH, '1.jpg')


@pytest.fixture
def produtos(db):
    image = SimpleUploadedFile(
        name='1.jpg', content=open(IMAGE_PATH, 'rb').read(), content_type='image/jpeg')
    produto = Produto(
        nomelongo='ÓLEO SW5',
        preco='25.00',
        foto=image,
        descricao='ÓLEO PARA CARRO FORD FIESTA'

    )

    produto.save()
    return [produto]


@pytest.fixture
def resp(client, produtos):
    return client.get(reverse('produtos:index'))


def test_status_code(resp):
    assert 200 == resp.status_code


@pytest.mark.parametrize(
    'content', [
        '25,00',
        'ÓLEO SW5',
        'ÓLEO PARA CARRO FORD FIESTA',
    ]
)
def test_index_content(resp, content):
    dj_assert_contains(resp, content)


def test_image_url(resp, produtos):
    produto = produtos[0]
    dj_assert_contains(resp, produto.foto.url)
