import pytest

from django.urls import reverse

from checklistos.django_assertions import dj_assert_contains

from checklistos.servicos.models import Servico


@pytest.fixture
def servicos(db):
    servico = Servico(
        nomelongo='Troca de óleo',
        preco='50.00',
        descricao='Serviço de troca de óleo'

    )

    servico.save()
    return [servico]


@pytest.fixture
def resp(client, servicos):
    return client.get(reverse('servicos:index'))


def test_status_code(resp):
    assert 200 == resp.status_code


@pytest.mark.parametrize(
    'content', [
        '50,00',
        'Troca de óleo',
        'Serviço de troca de óleo',
    ]
)
def test_index_content(resp, content):
    dj_assert_contains(resp, content)
