from django.shortcuts import render
from requests import head
from requests.exceptions import ConnectionError

from mocks.core.models import Congressperson


def home(request):
    context = {
        'congresspeople': Congressperson.objects.all(),
        'chamber_of_deputies': _is_chamber_of_deputies_on()
    }
    return render(request, 'core/index.html', context=context)


def _is_chamber_of_deputies_on():
    url = (
        'http://www2.camara.leg.br/'
        'transparencia/'
        'cota-para-exercicio-da-atividade-parlamentar/'
        'dados-abertos-cota-parlamentar/'
    )

    try:
        response = head(url)
    except ConnectionError:
        return False

    return 200 <= response.status_code < 500
